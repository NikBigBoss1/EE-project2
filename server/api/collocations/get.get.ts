import {CollocationSchema} from "~/server/models/collocation.schema";

export default defineEventHandler(async (event) => {
    try {
        return await CollocationSchema.find()
    }
    catch (error) {
        throw createError({
            statusCode: 500,
        })
    }
})