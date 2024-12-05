import { defineMongooseModel } from '#nuxt/mongoose'

export const CollocationSchema = defineMongooseModel({
    name: 'Collocation',
    schema: {
        collocation: {
            type: 'string',
            required: true,
        },
        type: {
            type: 'string',
            required: true,
        },
        choices: {
            type: ['string'],
            required: true,
        },
    },
})