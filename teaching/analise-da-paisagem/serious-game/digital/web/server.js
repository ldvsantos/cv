import pkg from 'boardgame.io/dist/cjs/server.js';
const { Server, Origins } = pkg;
import { RiskOfLandscapes } from './src/game/Game.js';

const server = Server({
  games: [RiskOfLandscapes],
  origins: [Origins.LOCALHOST_IN_DEVELOPMENT, 'http://localhost:5173'],
});

const PORT = process.env.PORT || 8000;
server.run(PORT, () => {
  console.log(`[server] Risk of Landscapes lobby on http://localhost:${PORT}`);
});
