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
  RECEIPT: apiUrl+"/receiptWithoutID",
  RECEIPT_LINE: apiUrl+"/receiptLine",
  RECEIPT_REPORT_BY_RECEIPTID: apiUrl+"/showReceiptReportByReceiptID",
  RECEIPT_REPORT_LINE_BY_RECEIPTID: apiUrl+"/showReceiptReportByReceiptIDLine",
  ROOM_SUMMARY_ROOMCAT: apiUrl+"/roomSummaryByRoomCat",
  ROOM_SUMMARY: apiUrl+"/roomSummary",
  ROOMSFREE: apiUrl+"/getAllRoomFreeByRoomCat",
  ROOM: apiUrl+"/room",
  CUSTOMER: apiUrl+"/customer",
  USERNAME: "username",
  USER_TYPE: "userType",
};
