import { Context, Next } from "https://deno.land/x/oak/mod.ts";
import * as tf from "https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.12.0/dist/tf.min.js";

export async function aiMiddleware(ctx: Context, next: Next) {
  // Initialize TensorFlow
  await tf.ready();
  
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