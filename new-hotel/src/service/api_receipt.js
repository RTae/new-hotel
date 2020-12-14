import httpClient from "@/service/httpClient";
import { server } from "@/service/constants";

export const createReceipt = async values => {
    var bodyFormData = new FormData();
    bodyFormData.append("customerID", values.customerID);
    bodyFormData.append("paymentMedId", values.paymentMedId);
    bodyFormData.append("cuponID", values.cuponID);
    bodyFormData.append("dateCreate", values.dateCreate);
    bodyFormData.append("paymentRef", values.paymentRef);
    bodyFormData.append("totalReceived", values.totalReceived);
    bodyFormData.append("remark", values.remark);
    const result = await httpClient.post(server.RECEIPT, bodyFormData);
    return result.data
};

export const createReceiptLine = async values =>{
    var bodyFormData = new FormData();
    bodyFormData.append("receiptID", values.receiptID);
    bodyFormData.append("invoiceID", values.invoiceID);
    bodyFormData.append("remark", values.remark);
    const result = await httpClient.post(server.RECEIPT_LINE, bodyFormData);
    return result.data
};