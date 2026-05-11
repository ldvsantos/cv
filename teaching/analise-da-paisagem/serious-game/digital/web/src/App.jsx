import React, { useState } from 'react';
import { Client } from 'boardgame.io/react';
import { SocketIO } from 'boardgame.io/multiplayer';
import { RiskOfLandscapes } from './game/Game.js';
import { Board } from './ui/Board.jsx';
import { Lobby } from './ui/Lobby.jsx';

const SERVER = `http://${window.location.hostname}:8000`;

function makeClient(numPlayers) {
  return Client({
    game: RiskOfLandscapes,
    board: Board,
    numPlayers,
    multiplayer: SocketIO({ server: SERVER }),
    debug: false,
  });
}

export default function App() {
  const [session, setSession] = useState(null);

  const handleStart = (s) => {
    sessionStorage.setItem('rol_matchID', s.matchID);
    setSession(s);
  };

  if (!session) return <Lobby onStart={handleStart} server={SERVER} />;

  const RiskClient = makeClient(session.numPlayers);
  return (
    <RiskClient
      matchID={session.matchID}
      playerID={String(session.playerID)}
      credentials={session.credentials}
    />
  );
}
