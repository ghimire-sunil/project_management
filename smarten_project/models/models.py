from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    project_id = fields.Many2one("project.project", string="Project")
    project_type_ids = fields.Many2many("custom.project.type", string="Project Type")

    def write(self, vals):
        res = super(CrmLead, self).write(vals)
        for lead in self:
            # Only trigger if stage changed to Won and no project yet
            if "stage_id" in vals:
                new_stage = self.env["crm.stage"].browse(vals["stage_id"])
                if new_stage.is_won and not lead.project_id:

                    if not lead.project_type_ids:
                        raise UserError(_("Please select at least one Project Type."))

                    # Pick first template as base
                    base_type = lead.project_type_ids[0]
                    if not base_type.project_template_id:
                        raise UserError(_("No template project configured for type: %s") % base_type.name)

                    # Create main project from the first template
                    main_project = base_type.project_template_id.copy({
                        "name": lead.partner_id.name or lead.name or "New Project",
                        "partner_id": lead.partner_id.id,
                        "user_id": lead.user_id.id,
                        "allow_timesheets": True,
                    })

                    # Merge other templates into the main project
                    for extra_type in lead.project_type_ids[1:]:
                        if not extra_type.project_template_id:
                            raise UserError(_("No template project configured for type: %s") % extra_type.name)

                        template = extra_type.project_template_id

                        # Copy stages (avoid duplicates by name)
                        for stage in template.type_ids:
                            existing_stage = main_project.type_ids.filtered(lambda s: s.name == stage.name)
                            if not existing_stage:
                                stage.copy({"project_ids": [(6, 0, [main_project.id])]})

                        # Copy tasks
                        for task in template.task_ids:
                            task.copy({
                                "project_id": main_project.id,
                                "stage_id": main_project.type_ids.filtered(lambda s: s.name == task.stage_id.name)[:1].id,
                            })

                    # Link project to lead
                    lead.project_id = main_project.id
        return res


class ProjectType(models.Model):
    _name = "custom.project.type"
    _description = "Project Type"

    name = fields.Char(string="Type", required=True)
    project_template_id = fields.Many2one("project.project", string="Template Project")
