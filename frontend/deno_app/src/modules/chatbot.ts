import { Context } from "https://deno.land/x/oak@v12.5.0/mod.ts";

export const chatbot = async (context: Context) => {
    const body = await context.request.body();
    const value = await body.value;
    const response = { reply: `You said: ${value.message}` };
    context.response.body = response;
}; 