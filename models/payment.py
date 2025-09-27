# from odoo import models

# class AccountPaymentRegister(models.TransientModel):
#     _inherit = "account.payment.register"

#     def _create_payments(self):
#         payments = super()._create_payments()

#         template = self.env.ref("account.mail_template_data_payment_receipt", raise_if_not_found=False)
#         if template:
#             for payment in payments:
#                 if payment.partner_id.email:
#                     template.send_mail(payment.id, force_send=True)

#         return payments

from odoo import models

class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    def _create_payments(self):
        payments = super()._create_payments()

        template = self.env.ref("account.mail_template_data_payment_receipt", raise_if_not_found=False)
        if template:
            for payment in payments:
                if payment.partner_id.email:
                    # Generate mail from template
                    mail_id = template.send_mail(payment.id, force_send=True)

                    # Log to chatter manually
                    if mail_id:
                        body = "Payment receipt email sent to %s" % (payment.partner_id.email)
                        payment.message_post(body=body, message_type="comment")

        return payments

