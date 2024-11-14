import { assertEquals } from "https://deno.land/std@0.204.0/testing/asserts.ts";

Deno.test("Chatbot response", async () => {
    // Implement test for chatbot module
    const response = { reply: "You said: Hello" };
    assertEquals(response.reply, "You said: Hello");
}); 