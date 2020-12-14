import httpClient from "@/service/httpClient";
import { server } from "@/service/constants";

export const roomFree = async (roomCatID, limit) => {
    return httpClient.get(server.ROOMSFREE + "?roomCatID=" + roomCatID + "&limit=" + limit);
}

export const createRoom = async (value) => {
    
    bodyFormData.append("roomCatID", values.roomCatID);
    bodyFormData.append("status", values.status);
    bodyFormData.append("cleanStatus", values.cleanStatus);
    const result = await httpClient.put(server.ROOM_WITH_OUT_ID, bodyFormData);
    return result.data
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

export const deleteRoom = async (id) => {
    const result = await httpClient.delete(server.ROOM + "/" + id );
    return result.data
}

export const roomSummaryByRoomCat = async () => {
    const result = await httpClient.get(server.ROOM_SUMMARY_ROOMCAT);
    return result
}

export const roomSummary = async () => {
    const result = await httpClient.get(server.ROOM_SUMMARY);
    return result
}