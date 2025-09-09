<section id="workflow-health" class="card">
  <h2>Workflow Health — Task Sheet</h2>
  <div id="wf-summary"></div>
  <table id="wf-table">
    <thead>
      <tr>
        <th>When (UTC)</th><th>Repo</th><th>Workflow</th><th>Run</th><th>Branch</th>
        <th>Status</th><th>Conclusion</th><th>Duration (s)</th><th>SLA</th><th>Link</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>
</section>

<script>
// Lightweight CSV fetcher
async function fetchCSV(url) {
  const res = await fetch(url, { cache: 'no-store' });
  const text = await res.text();
  const [header, ...rows] = text.trim().split(/\r?\n/);
  const keys = header.split(',');
  return rows.map(r => {
    // naive CSV split (fine for our simple seed; upgrade if needed)
    const vals = r.split(/,(?=(?:[^"]*"[^"]*")*[^"]*$)/).map(v => v.replace(/^"|"$/g,''));
    return Object.fromEntries(keys.map((k,i)=>[k, vals[i] ?? '']));
  });
}

function pill(txt) {
  const ok = txt === 'success';
  const fail = ['failure','cancelled','timed_out'].includes(txt);
  const color = ok ? '#10b981' : (fail ? '#ef4444' : '#f59e0b');
  return `<span style="padding:2px 8px;border-radius:999px;background:${color};color:white;font-size:12px;">${txt||'—'}</span>`;
}

function emojiSLA(met) { return met === 'true' || met === true ? '🟢' : '🔴'; }

(async () => {
  const data = await fetchCSV('data/ops/workflow_runs.csv');

  // Summary: success rate & MTTR (for failed runs only)
  const total = data.length;
  const successes = data.filter(d=>d.conclusion==='success').length;
  const failRuns = data.filter(d=>d.conclusion && d.conclusion !== 'success');
  const successRate = total ? Math.round((successes/total)*100) : 0;
  const mttr = failRuns.length
    ? Math.round(failRuns.reduce((a,d)=>a + (parseInt(d.duration_sec||0)||0),0) / failRuns.length)
    : 0;

  document.getElementById('wf-summary').innerHTML =
    `<p><strong>Success rate:</strong> ${successRate}% &nbsp; | &nbsp; <strong>MTTR (failed runs):</strong> ${mttr}s &nbsp; | &nbsp; <strong>Total runs:</strong> ${total}</p>`;

  // Table rows
  const tbody = document.querySelector('#wf-table tbody');
  tbody.innerHTML = data
    .sort((a,b)=> new Date(b.started_at) - new Date(a.started_at))
    .map(d => `
      <tr>
        <td>${(d.started_at||'').replace('T',' ').replace('Z','')}</td>
        <td>${d.repo||'—'}</td>
        <td>${d.workflow_name||'—'}</td>
        <td>${d.run_id||'—'}</td>
        <td>${d.branch||'—'}</td>
        <td>${pill(d.status||'—')}</td>
        <td>${pill(d.conclusion||'—')}</td>
        <td>${d.duration_sec||'—'}</td>
        <td>${emojiSLA(d.sla_met)}</td>
        <td><a href="${d.url||'#'}" target="_blank" rel="noopener">open</a></td>
      </tr>
    `).join('');
})();
</script>
