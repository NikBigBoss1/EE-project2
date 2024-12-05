import { defineEventHandler } from 'h3';
import { ResultSchema } from '~/server/models/result.schema';
import mongoose from 'mongoose';

export default defineEventHandler(async (event) => {
  try {
    const body = await readBody(event);

    const Result = mongoose.model('Result', ResultSchema.schema);

    const newResult = new Result(body);
    const result = await newResult.save();

    return { success: true, result: result };
  } catch (err: unknown) {
    return { success: false, error: err instanceof Error ? err.message : 'Unknown error' };
  }
});