import {ResultSchema} from "~/server/models/result.schema";

export default defineEventHandler(async (event) => {
    try {
        return await ResultSchema.find()
    }
    catch (error) {
        throw createError({
            statusCode: 500,
        })
    }
})