from odoo import models, fields, api, _
from odoo.exceptions import UserError

class HrContract(models.Model):
    _inherit = 'hr.contract'

    insentif_pekerjaan = fields.Monetary('Insntif Pekerjaan', compute='_get_task', default=0)
    easy = fields.Float(string='Easy')
    medium = fields.Float(string='Medium')
    hard = fields.Float(string='Hard')
    very_easy = fields.Float(string='Very Easy')
    # field_name_id = fields.Many2one('project.tags', string='field_name')

    def _get_task(self):
        print('sda')
        all_task = self.env['project.task'].search([('user_ids', '=', self.employee_id.user_id.id), ('stage_id.name', '=', 'Done'), ('active','=', True)])
        tag_easy = self.env['project.tags'].search([('name', '=', 'Easy')])
        tag_medium = self.env['project.tags'].search([('name', '=', 'Medium')])
        tag_hard = self.env['project.tags'].search([('name', '=', 'Hard')])
        tag_very_easy = self.env['project.tags'].search([('name', '=', 'Very Easy')])
        easy = len(all_task.filtered(lambda x: x.tag_ids.id == tag_easy.id)) * self.easy
        medium = len(all_task.filtered(lambda x: x.tag_ids.id == tag_medium.id)) * self.medium
        hard = len(all_task.filtered(lambda x: x.tag_ids.id == tag_hard.id)) * self.hard
        very_easy = len(all_task.filtered(lambda x: x.tag_ids.id == tag_very_easy.id)) * self.very_easy
        if len(all_task) > 0:
            self.insentif_pekerjaan = easy + medium + hard + very_easy
        else:
            self.insentif_pekerjaan = 0


class HrPay(models.Model):
    _inherit = 'hr.payslip'
    ta = fields.Char(string='Task')
    task_ids = fields.Many2many(comodel_name='project.task', string='Task', domain=['|', ('active', '=', True), ('active', '=', False)], context={'active_test': False})
    
    
    def compute_sheet(self):
        for payslip in self:
            number = payslip.number or self.env['ir.sequence'].next_by_code(
                'salary.slip')
            # delete old payslip lines
            payslip.line_ids.unlink()
            # set the list of contract for which the rules have to be applied
            # if we don't give the contract, then the rules to apply should be for all current contracts of the employee
            contract_ids = payslip.contract_id.ids or \
                           self.get_contract(payslip.employee_id,
                                             payslip.date_from, payslip.date_to)
            lines = [(0, 0, line) for line in
                     self._get_payslip_lines(contract_ids, payslip.id)]
            payslip.write({'line_ids': lines, 'number': number})
            task_ids = self.env['project.task'].search([('user_ids', '=', self.employee_id.user_id.id), ('stage_id.name', '=', 'Done'), ('active','=', True)]).mapped('id')
            payslip.write({'task_ids': [(6,0,task_ids)]})
        return True

    def action_payslip_done(self):
        self.compute_sheet()
        # all_task = self.env['project.task'].search([('user_ids', '=', self.employee_id.user_id.id), ('stage_id.name', '=', 'Done')])
        for task in self.task_ids:
            task.write({
                'active': 0,
                # 'pay_id':self.id
            })
        # self.task_ids = ','.join(all_task.mapped('id'))
        return self.write({'state': 'done'})
    
    # def view_task(self):
    #     return {
    #             'type': 'ir.actions.act_window',
    #             'name': 'Task '+self.name,
    #             'view_mode': 'tree,kanban',
    #             'res_model': 'project.task',
    #             'domain': [('id','in',self.task_ids.mapped('id'))]
    #         }
    
# class Task(models.Model):
#     _inherit = 'project.task'
#     pay_id = fields.Char(string='Pay')

    

    
        
    


    