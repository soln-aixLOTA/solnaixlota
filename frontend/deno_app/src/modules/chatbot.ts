import { Context } from "https://deno.land/x/oak/mod.ts";

export const chatbot = async (context: Context) => {
    const { value } = await context.request.body();
    const response = { reply: `You said: ${value.message}` };
    context.response.body = response;
}; 