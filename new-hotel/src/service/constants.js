export const NETWORK_CONNECTION_MESSAGE =
  "Cannot connect to server, Please try again.";
export const NETWORK_TIMEOUT_MESSAGE =
  "A network timeout has occurred, Please try again.";
export const UPLOAD_PHOTO_FAIL_MESSAGE =
  "An error has occurred. The photo was unable to upload.";
export const NOT_CONNECT_NETWORK = "NOT_CONNECT_NETWORK";

export const apiUrl = "https://new-hotel-backend.vercel.app";

export const server = {
  LOGIN_URL: apiUrl + "/login",
  REGISTER_URL: apiUrl + "/register",
  SEARCH: apiUrl+ "/customerEmail",
  INVOICE: apiUrl+"/invoiceWithoutID",
  INVOICE_LINE: apiUrl+"/invoiceLine",
  INVOICE_SUMMARY: apiUrl+"/summaryInvoice",
  RECEIPT: apiUrl+"/receiptWithoutID",
  GET_RECEIPT_BY_CUSTOMER_ID: apiUrl+"/readByCustomerID",
  RECEIPT_LINE: apiUrl+"/receiptLine",
  RECEIPT_REPORT_BY_RECEIPTID: apiUrl+"/showReceiptReportByReceiptID",
  RECEIPT_REPORT_LINE_BY_RECEIPTID: apiUrl+"/showReceiptReportByReceiptIDLine",
  RECEIPT_SUMMARY: apiUrl+"/receiptSummary",
  ROOM_SUMMARY_ROOMCAT: apiUrl+"/roomSummaryByRoomCat",
  ROOM_SUMMARY: apiUrl+"/roomSummary",
  ROOMSFREE: apiUrl+"/getAllRoomFreeByRoomCat",
  ROOM: apiUrl+"/room",
  LOGIN: apiUrl+"/login",
  ROOM_WITH_OUT_ID: apiUrl+"/roomWithOutID",
  CUSTOMER: apiUrl+"/customer",
  CLEANING_GET_ALL: apiUrl+"/getAllCleaning",
  USERNAME: "username",
  USER_TYPE: "userType",
};
