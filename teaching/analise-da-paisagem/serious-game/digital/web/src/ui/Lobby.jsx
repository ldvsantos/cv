import React, { useEffect, useState } from 'react';
import { LobbyClient } from 'boardgame.io/client';

export function Lobby({ onStart, server }) {
  const [client] = useState(() => new LobbyClient({ server }));
  const [name, setName] = useState('');
  const [numPlayers, setNumPlayers] = useState(3);
  const [matches, setMatches] = useState([]);
  const [manualId, setManualId] = useState('');

  // ?match=XYZ no link automatico
  useEffect(() => {
    const url = new URL(window.location.href);
    const m = url.searchParams.get('match');
    if (m) setManualId(m);
  }, []);

  const refresh = async () => {
    try {
      const { matches } = await client.listMatches('risk-of-landscapes');
      setMatches(matches);
    } catch (e) { console.warn('lobby:', e.message); }
  };

  useEffect(() => { refresh(); const t = setInterval(refresh, 3000); return () => clearInterval(t); }, []);

  async function createMatch() {
    if (!name.trim()) return alert('Informe seu nome.');
    const { matchID } = await client.createMatch('risk-of-landscapes', { numPlayers });
    await joinMatch(matchID, numPlayers);
  }

  async function joinMatch(matchID, np) {
    if (!name.trim()) return alert('Informe seu nome.');
    let match;
    try { match = await client.getMatch('risk-of-landscapes', matchID); }
    catch { return alert('Partida não encontrada. Confira o ID.'); }
    const slot = match.players.find((p) => !p.name);
    if (!slot) return alert('Partida cheia.');
    const { playerCredentials } = await client.joinMatch('risk-of-landscapes', matchID, {
      playerID: String(slot.id), playerName: name,
    });
    onStart({ matchID, playerID: slot.id, credentials: playerCredentials,
              numPlayers: np ?? match.players.length });
  }

  async function joinByManualId() {
    if (!manualId.trim()) return alert('Cole o ID da partida.');
    const id = manualId.trim();
    try {
      const match = await client.getMatch('risk-of-landscapes', id);
      await joinMatch(id, match.players.length);
    } catch { alert('Partida não encontrada com esse ID.'); }
  }

  return (
    <div className="lobby">
      <h1>🐉 Risk of Landscapes</h1>
      <p style={{ color: 'var(--muted)', fontSize: 13 }}>
        Serious Game multiplayer · Análise da Paisagem · UEFS
      </p>

      <div className="row">
        <label>Seu nome</label>
        <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Ex.: Diego" />
      </div>

      <hr style={{ border: '1px solid var(--border)', margin: '16px 0' }} />

      <h3 style={{ fontSize: 14, marginBottom: 6 }}>① Criar nova partida</h3>
      <div className="row">
        <label>Nº jogadores</label>
        <select value={numPlayers} onChange={(e) => setNumPlayers(Number(e.target.value))}>
          {[2,3,4,5,6].map((n) => <option key={n} value={n}>{n}</option>)}
        </select>
        <button onClick={createMatch}>Criar partida</button>
      </div>
      <p style={{ fontSize: 11, color: 'var(--muted)', marginTop: 4 }}>
        Após criar, você verá um <b>link/ID de convite</b> dentro do jogo para enviar aos outros jogadores.
      </p>

      <hr style={{ border: '1px solid var(--border)', margin: '16px 0' }} />

      <h3 style={{ fontSize: 14, marginBottom: 6 }}>② Entrar com ID de convite</h3>
      <div className="row">
        <input value={manualId} onChange={(e) => setManualId(e.target.value)}
               placeholder="cole o ID da partida aqui" style={{ flex: 1 }} />
        <button onClick={joinByManualId}>Entrar</button>
      </div>

      <hr style={{ border: '1px solid var(--border)', margin: '16px 0' }} />

      <div className="matches">
        <h3 style={{ fontSize: 14, marginBottom: 6 }}>③ Partidas abertas (mesma rede)</h3>
        {matches.length === 0 && <p style={{ color: 'var(--muted)', fontSize: 12 }}>Nenhuma partida no momento.</p>}
        {matches.map((m) => {
          const taken = m.players.filter((p) => p.name).length;
          return (
            <div key={m.matchID} className="match-item">
              <div>
                <code>{m.matchID.slice(0, 8)}</code> · {taken}/{m.players.length} jogadores
                {m.gameover && ' · 🏁 finalizada'}
              </div>
              <button disabled={taken >= m.players.length || m.gameover}
                      onClick={() => joinMatch(m.matchID, m.players.length)}>
                Entrar
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
}
