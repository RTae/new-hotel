import * as userAPI from "../service/api_user"
import * as invoiceAPI from "../service/api_invoice"
import * as roomAPI from "../service/api_room"
import * as receiptAPI from "../service/api_receipt"

export default {
  ...userAPI,
  ...invoiceAPI,
  ...roomAPI,
  ...receiptAPI
};
