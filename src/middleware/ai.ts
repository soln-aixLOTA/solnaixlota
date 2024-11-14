import { Context, Next } from "fresh/server.ts";
import * as tf from "tensorflow/tf.ts";

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