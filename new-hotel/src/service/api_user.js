import httpClient from "@/service/httpClient";
import { server } from "@/service/constants";

export const register = async values => {
  var bodyFormData = new FormData();
  bodyFormData.append("firstname", values.firstname);
  bodyFormData.append("familyname", values.familyname);
  bodyFormData.append("email", values.email);
  bodyFormData.append("phoneNumber", values.phoneNumber);
  bodyFormData.append("creditCardNumber", values.creditCardNumber);
  bodyFormData.append("point", values.point);
  bodyFormData.append("password", values.password);

  const result = await httpClient.post(server.REGISTER_URL, bodyFormData);
  if (result.data.status === "1") {
    return result.data
  } else {
    return result.data
  }
};