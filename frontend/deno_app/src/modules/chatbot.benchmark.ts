import { benchmark } from "https://deno.land/x/bench@0.2.3/mod.ts";
import { chatbot } from "./chatbot.ts";
import { createMockContext } from "https://deno.land/x/oak@v10.6.0/testing.ts";

benchmark({
    name: "Chatbot Response Time",
    fn: async () => {
        const context = createMockContext({
            request: {
                body: async () => ({ value: { message: "Performance Test" } }),
            },
        });
        await chatbot(context);
    },
    runs: 1000,
}); 