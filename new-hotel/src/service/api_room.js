import httpClient from "@/service/httpClient";
import { server } from "@/service/constants";

export const roomFree = async (roomCatID, limit) => {
    return httpClient.get(server.ROOMSFREE + "?roomCatID=" + roomCatID + "&limit=" + limit);
}

export const updateRoom = async (values) => {
    var bodyFormData = new FormData();
    bodyFormData.append("roomID", values.roomID);
    bodyFormData.append("roomCatID", values.roomCatID);
    bodyFormData.append("status", values.status);
    bodyFormData.append("cleanStatus", values.cleanStatus);

    const result = await httpClient.put(server.ROOM, bodyFormData);
    return result.data
}