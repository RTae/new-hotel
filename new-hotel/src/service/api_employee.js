import httpClient from "@/service/httpClient";
import { server } from "@/service/constants";

export const getAllCleaning = async () => {
  const result = await httpClient.get(server.CLEANING_GET_ALL);
  return result
}