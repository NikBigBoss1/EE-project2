import { defineMongooseModel } from '#nuxt/mongoose';
import { Schema } from 'mongoose';


export const SubCollocationSchema = defineMongooseModel({
  name: 'subCollocation',
  schema: {
    type: {
      type: 'string',
      required: true,
    },
    collocation: {
      type: 'string',
      required: true,
    },
    firstGuess: {
      type: Schema.Types.Boolean,
      required: true,
    },
    time: {
        type: Schema.Types.Number,
      required: true,
    },
  },
});

export const ResultSchema = defineMongooseModel({
  name: 'Result',
  schema: {
    experience: {
      type: 'string',
      required: true,
    },
    gender: {
      type: 'string',
      required: true,
    },
    englishProficiency: {
      type: 'string',
      required: true,
    },
    age: {
      type: Schema.Types.Number,
      required: true,
    },
    collocations: {
      type: [SubCollocationSchema.schema],
      required: true,
    },
  },
});