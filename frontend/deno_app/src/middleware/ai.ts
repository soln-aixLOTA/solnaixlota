import { Context, Next } from "https://deno.land/x/oak@v12.5.0/mod.ts";
import * as tf from "https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.12.0/dist/tf.esm.js";

export async function aiMiddleware(ctx: Context, next: Next) {
  // Initialize TensorFlow (if necessary)
  // await tf.ready(); // Remove or replace based on TensorFlow.js docs
  
  // Add AI context to state
  ctx.state.ai = {
    tf,
    models: new Map(),
    inferenceCount: 0,
  };

  // Performance monitoring
  const start = performance.now();
  await next();
  const ms = performance.now() - start;
  
  ctx.response.headers.set("X-Response-Time", `${ms}ms`);
} 