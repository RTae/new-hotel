import httpClient from "@/service/httpClient";
import { server } from "@/service/constants";

export const createInvoice = async values => {
    var bodyFormData = new FormData();
    bodyFormData.append("roomCatID", values.roomCatID);
    bodyFormData.append("customerID", values.customerID);
    bodyFormData.append("dateCreate", values.dateCreate);
    bodyFormData.append("total", values.total);
    bodyFormData.append("vat", values.vat);
    bodyFormData.append("checkIn", values.checkIn);
    bodyFormData.append("checkOut", values.checkOut);
    bodyFormData.append("numberOfRoom", values.numberOfRoom);
  
    const result = await httpClient.post(server.INVOICE, bodyFormData);
    if (result.data.status === "1") {
      return result.data
    } else {
      return result.data
    }
  };

  export const createInvoiceLine = async values => {
    var bodyFormData = new FormData();
    bodyFormData.append("invoiceID", values.invoiceID);
    bodyFormData.append("roomID", values.roomID);
    bodyFormData.append("remark", values.remark);

    const result = await httpClient.post(server.INVOICE_LINE, bodyFormData);
    return result.data
  }