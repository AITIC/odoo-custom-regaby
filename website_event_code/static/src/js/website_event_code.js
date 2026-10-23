import { rpc } from "@web/core/network/rpc";
import { registry } from "@web/core/registry";
import { Interaction } from "@web/public/interaction";

export class EventCodeSubmit extends Interaction {
    static selector = "form.o_wevent_registration";
    dynamicContent = {
        ".a-submit": {
            "t-on-click.prevent.stop": this.onSubmitClick,
        },
    };

    /**
     * @param {MouseEvent} ev
     */
    async onSubmitClick(ev) {
        const formEl = ev.currentTarget.closest("form");
        const formData = Object.fromEntries(new FormData(formEl));

        const modal = await this.waitFor(rpc(
            formEl.action,
            formData,
        ));

        const modalEl = new DOMParser().parseFromString(modal, "text/html").body.firstChild;
        if (modalEl) {
            this.insert(modalEl, document.body);
        }
    }
}

registry
    .category("public.interactions")
    .add("website_event_code.event_code_submit", EventCodeSubmit);
