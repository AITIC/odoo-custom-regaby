import { patch } from "@web/core/utils/patch";
import { InvoiceButton } from "@point_of_sale/app/screens/ticket_screen/invoice_button/invoice_button";

patch(InvoiceButton.prototype, {
    async _downloadInvoice(orderId) {
        if (!this.pos.config.print_pdf_invoice) {
            // Skip PDF download when the flag is disabled; just load the order
            const orders = await this.pos.data.loadServerOrders([["id", "=", orderId]]);
            return orders[0];
        }
        return super._downloadInvoice(orderId);
    },
});
