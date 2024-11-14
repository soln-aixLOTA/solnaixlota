import * as tf from "tensorflow/tf.ts";

export class ModelLoader {
  private modelCache = new Map<string, tf.LayersModel>();

  async loadModel(modelPath: string): Promise<tf.LayersModel> {
    if (this.modelCache.has(modelPath)) {
      return this.modelCache.get(modelPath)!;
    }

    try {
      const model = await tf.loadLayersModel(modelPath);
      this.modelCache.set(modelPath, model);
      return model;
    } catch (error) {
      if (error instanceof Error) {
        throw new Error(`Failed to load model from ${modelPath}: ${error.message}`);
      } else {
        throw new Error(`Failed to load model from ${modelPath}: Unknown error`);
      }
    }
  }

  async predict(modelPath: string, input: tf.Tensor): Promise<tf.Tensor> {
    const model = await this.loadModel(modelPath);
    if (!model) {
      throw new Error(`Model not loaded for ${modelPath}`);
    }
    return model.predict(input) as tf.Tensor;
  }

  async unloadModel(modelPath: string): Promise<void> {
    if (this.modelCache.has(modelPath)) {
      this.modelCache.delete(modelPath);
    }
  }

  async clearCache(): Promise<void> {
    this.modelCache.clear();
  }

  async disposeModel(modelPath: string): Promise<void> {
    if (this.modelCache.has(modelPath)) {
      const model = this.modelCache.get(modelPath);
      if (model) {
        await model.dispose();
      }
      this.modelCache.delete(modelPath);
    }
  }

  async disposeAllModels(): Promise<void> {
    for (const model of this.modelCache.values()) {
      await model.dispose();
    }
    this.modelCache.clear();
  }
}