import { HealthCheck } from './types';

export const performHealthCheck = async (): Promise<HealthCheck> => {
  const checks = {
    database: await checkDatabase(),
    redis: await checkRedis(),
    aiServices: await checkAIServices(),
  };
  
  return {
    status: Object.values(checks).every(check => check.status === 'healthy') 
      ? 'healthy' 
      : 'unhealthy',
    checks,
    timestamp: new Date().toISOString(),
  };
}; 