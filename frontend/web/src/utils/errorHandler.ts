export class AppError extends Error {
  constructor(
    public readonly code: string,
    message: string,
    public readonly details?: unknown
  ) {
    super(message);
    this.name = 'AppError';
  }
}

export const errorHandler = (error: unknown): AppError => {
  if (error instanceof AppError) {
    return error;
  }
  
  if (error instanceof Error) {
    return new AppError('UNKNOWN_ERROR', error.message);
  }
  
  return new AppError('UNKNOWN_ERROR', 'An unknown error occurred');
}; 