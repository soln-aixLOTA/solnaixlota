import { HandlerContext } from "fresh/server.ts";
import { ModelLoader } from "@/services/model-loader.ts";

const modelLoader = new ModelLoader();

export async function handler(req: Request, ctx: HandlerContext) {
  if (req.method !== "POST") {
    return new Response("Method not allowed", { status: 405 });
  }

  try {
    const body = await req.json();
    const { modelPath, input } = body;

    if (!modelPath || !input) {
      return new Response("Missing required fields", { status: 400 });
    }

    const inputTensor = ctx.state.ai.tf.tensor(input);
    const prediction = await modelLoader.predict(modelPath, inputTensor);
    const result = await prediction.array();

    return new Response(JSON.stringify({ prediction: result }), {
      headers: { "Content-Type": "application/json" },
    });
  } catch (error) {
    return new Response(`Error: ${error.message}`, { status: 500 });
  }
} 