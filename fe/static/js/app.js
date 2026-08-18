/**
 * HR Assistant - Frontend JavaScript
 */

// State
let currentPage = 'chat';
let messages = [];
let isLoading = false;

// DOM Elements
const pages = document.querySelectorAll('.page');
const navItems = document.querySelectorAll('.nav-item');
const messagesContainer = document.getElementById('messages');
const emptyState = document.getElementById('empty-state');
const chatForm = document.getElementById('chat-form');
const questionInput = document.getElementById('question-input');
const sendBtn = document.getElementById('send-btn');
const debugPanel = document.getElementById('debug-panel');
const debugContent = document.getElementById('debug-content');
const toggleDebugBtn = document.getElementById('toggle-debug');
const statusDot = document.getElementById('status-dot');
const statusText = document.getElementById('status-text');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    lucide.createIcons();
    initNavigation();
    initChatForm();
    initDebugPanel();
    initStarterQuestions();
    checkStatus();
    loadMetrics();
});

// Navigation
function initNavigation() {
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const page = item.dataset.page;
            navigateTo(page);
        });
    });
}

function navigateTo(page) {
    currentPage = page;

    // Update nav
    navItems.forEach(item => {
        item.classList.toggle('active', item.dataset.page === page);
    });

    // Update pages
    pages.forEach(p => {
        p.classList.toggle('hidden', p.id !== `page-${page}`);
    });

    // Load page content
    if (page === 'metrics') {
        loadMetrics();
    }
}

// Chat
function initChatForm() {
    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const question = questionInput.value.trim();
        if (!question || isLoading) return;

        // Add user message
        addMessage('user', question);
        questionInput.value = '';

        // Show loading
        setLoading(true);
        showDebugLoading();

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question })
            });

            const data = await response.json();

            if (data.error) {
                addMessage('assistant', `Lỗi: ${data.error}`);
                updateDebugPanel({ error: data.error });
            } else {
                addMessage('assistant', data.answer);
                updateDebugPanel(data);
            }
        } catch (error) {
            addMessage('assistant', 'Không thể kết nối server. Kiểm tra xem Flask đang chạy chưa.');
            updateDebugPanel({ error: error.message });
        } finally {
            setLoading(false);
        }
    });
}

function addMessage(role, content) {
    // Hide empty state
    emptyState.classList.add('hidden');

    const messageEl = document.createElement('div');
    messageEl.className = `message ${role}`;

    const time = new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });

    messageEl.innerHTML = `
        <div class="message-bubble">
            <div class="message-content">${escapeHtml(content)}</div>
        </div>
        <div class="message-time">${time}</div>
    `;

    messagesContainer.appendChild(messageEl);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function setLoading(loading) {
    isLoading = loading;
    sendBtn.disabled = loading;
    questionInput.disabled = loading;

    if (loading) {
        sendBtn.innerHTML = '<span class="loading-dots"><span></span><span></span><span></span></span>';
    } else {
        sendBtn.innerHTML = '<i data-lucide="send" class="w-5 h-5"></i><span>Gửi</span>';
        lucide.createIcons();
    }
}

// Debug Panel
function initDebugPanel() {
    toggleDebugBtn.addEventListener('click', () => {
        debugPanel.classList.toggle('collapsed');
        const icon = toggleDebugBtn.querySelector('i');
        icon.setAttribute('data-lucide', debugPanel.classList.contains('collapsed') ? 'chevron-left' : 'chevron-right');
        lucide.createIcons();
    });
}

function showDebugLoading() {
    debugContent.innerHTML = `
        <div class="flex items-center gap-3 text-secondary">
            <span class="loading-dots"><span></span><span></span><span></span></span>
            <span>Đang xử lý...</span>
        </div>
    `;
}

function updateDebugPanel(data) {
    if (data.error) {
        debugContent.innerHTML = `
            <div class="bg-red-50 border border-red-200 rounded-lg p-3">
                <p class="text-danger text-sm">${escapeHtml(data.error)}</p>
            </div>
        `;
        return;
    }

    let html = '';

    // Timing
    if (data.timing) {
        html += `
            <div class="mb-4">
                <h4 class="text-sm font-medium mb-2 flex items-center gap-2">
                    <i data-lucide="clock" class="w-4 h-4"></i>
                    Timing
                </h4>
                <div class="bg-slate-50 rounded-lg p-3 space-y-1 text-xs font-mono">
                    ${Object.entries(data.timing).map(([k, v]) => `
                        <div class="flex justify-between">
                            <span class="text-secondary">${k}:</span>
                            <span class="text-primary">${v}ms</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    // Scores
    if (data.scores) {
        html += `
            <div class="mb-4">
                <h4 class="text-sm font-medium mb-2 flex items-center gap-2">
                    <i data-lucide="bar-chart" class="w-4 h-4"></i>
                    Search Scores
                </h4>
                <div class="space-y-2">
                    ${data.scores.bm25 ? `
                        <div class="flex justify-between items-center">
                            <span class="text-sm text-secondary">BM25</span>
                            <span class="${getScoreClass(data.scores.bm25)}">${data.scores.bm25.toFixed(3)}</span>
                        </div>
                    ` : ''}
                    ${data.scores.dense ? `
                        <div class="flex justify-between items-center">
                            <span class="text-sm text-secondary">Dense</span>
                            <span class="${getScoreClass(data.scores.dense)}">${data.scores.dense.toFixed(3)}</span>
                        </div>
                    ` : ''}
                    ${data.scores.rrf ? `
                        <div class="flex justify-between items-center">
                            <span class="text-sm text-secondary">RRF</span>
                            <span class="${getScoreClass(data.scores.rrf)}">${data.scores.rrf.toFixed(3)}</span>
                        </div>
                    ` : ''}
                    ${data.scores.rerank ? `
                        <div class="flex justify-between items-center">
                            <span class="text-sm text-secondary">Rerank</span>
                            <span class="${getScoreClass(data.scores.rerank)}">${data.scores.rerank.toFixed(3)}</span>
                        </div>
                    ` : ''}
                </div>
            </div>
        `;
    }

    // Chunks
    if (data.chunks && data.chunks.length > 0) {
        html += `
            <div>
                <h4 class="text-sm font-medium mb-2 flex items-center gap-2">
                    <i data-lucide="layers" class="w-4 h-4"></i>
                    Retrieved Chunks (${data.chunks.length})
                </h4>
                <div class="space-y-2">
                    ${data.chunks.map((chunk, i) => `
                        <div class="chunk-card">
                            <div class="chunk-header" onclick="this.parentElement.classList.toggle('expanded')">
                                <span class="text-sm font-medium">Chunk ${i + 1}</span>
                                <i data-lucide="chevron-right" class="w-4 h-4 transition-transform"></i>
                            </div>
                            <div class="chunk-body">
                                <p class="text-xs text-secondary mb-2">${chunk.metadata?.source || 'Unknown source'}</p>
                                <p class="text-sm">${escapeHtml(chunk.text.substring(0, 300))}${chunk.text.length > 300 ? '...' : ''}</p>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    debugContent.innerHTML = html || '<p class="text-sm text-muted">No debug info available</p>';
    lucide.createIcons();
}

function getScoreClass(score) {
    if (score >= 0.8) return 'score-badge score-high';
    if (score >= 0.5) return 'score-badge score-medium';
    return 'score-badge score-low';
}

// Starter Questions
function initStarterQuestions() {
    document.querySelectorAll('.starter-q').forEach(btn => {
        btn.addEventListener('click', () => {
            questionInput.value = btn.dataset.question;
            questionInput.focus();
        });
    });
}

// Status
async function checkStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();

        if (data.pipeline_ready && data.qdrant) {
            statusDot.className = 'w-2 h-2 rounded-full bg-success';
            statusText.textContent = 'Ready';
        } else {
            statusDot.className = 'w-2 h-2 rounded-full bg-warning';
            statusText.textContent = data.pipeline_ready ? 'Qdrant offline' : 'Pipeline error';
        }
    } catch (error) {
        statusDot.className = 'w-2 h-2 rounded-full bg-danger';
        statusText.textContent = 'Server offline';
    }
}

// Metrics
async function loadMetrics() {
    const metricsGrid = document.getElementById('metrics-grid');
    const improvementTbody = document.getElementById('improvement-tbody');
    const failuresList = document.getElementById('failures-list');

    try {
        const response = await fetch('/api/metrics');
        const data = await response.json();

        const metrics = data.aggregate || {};
        const naiveMetrics = {
            faithfulness: 0.65,
            answer_relevancy: 0.58,
            context_precision: 0.52,
            context_recall: 0.61
        };

        // Score Cards
        metricsGrid.innerHTML = Object.entries(metrics).map(([key, value]) => {
            const labels = {
                faithfulness: 'Faithfulness',
                answer_relevancy: 'Answer Relevancy',
                context_precision: 'Context Precision',
                context_recall: 'Context Recall'
            };
            const percentage = (value * 100).toFixed(0);
            const color = value >= 0.7 ? '#22c55e' : value >= 0.5 ? '#f59e0b' : '#ef4444';

            return `
                <div class="metric-card">
                    <div class="metric-value" style="color: ${color}">${percentage}%</div>
                    <div class="metric-label">${labels[key] || key}</div>
                    <div class="metric-bar">
                        <div class="metric-bar-fill" style="width: ${percentage}%; background: ${color}"></div>
                    </div>
                </div>
            `;
        }).join('');

        // Improvement Table
        improvementTbody.innerHTML = Object.entries(metrics).map(([key, value]) => {
            const labels = {
                faithfulness: 'Faithfulness',
                answer_relevancy: 'Answer Relevancy',
                context_precision: 'Context Precision',
                context_recall: 'Context Recall'
            };
            const naive = naiveMetrics[key] || 0;
            const delta = value - naive;
            const deltaClass = delta >= 0 ? 'text-success' : 'text-danger';

            return `
                <tr class="border-b border-slate-100">
                    <td class="py-2 px-3">${labels[key] || key}</td>
                    <td class="py-2 px-3 text-right">${(naive * 100).toFixed(0)}%</td>
                    <td class="py-2 px-3 text-right font-medium">${(value * 100).toFixed(0)}%</td>
                    <td class="py-2 px-3 text-right ${deltaClass}">${delta >= 0 ? '+' : ''}${(delta * 100).toFixed(0)}%</td>
                </tr>
            `;
        }).join('');

        // Failures
        failuresList.innerHTML = data.failures && data.failures.length > 0 ? data.failures.map(f => `
            <div class="border border-slate-200 rounded-lg p-3">
                <p class="text-sm font-medium mb-2">${escapeHtml(f.question)}</p>
                <div class="flex gap-2 flex-wrap">
                    <span class="text-xs px-2 py-1 bg-red-50 text-danger rounded">${f.worst_metric}: ${(f.score * 100).toFixed(0)}%</span>
                    <span class="text-xs px-2 py-1 bg-slate-100 text-secondary rounded">avg: ${(f.avg_score * 100).toFixed(0)}%</span>
                </div>
            </div>
        `).join('') : '<p class="text-sm text-muted">No failure data available</p>';

    } catch (error) {
        console.error('Failed to load metrics:', error);
        metricsGrid.innerHTML = '<p class="text-sm text-danger col-span-4">Failed to load metrics</p>';
    }
}

// Pipeline Steps
document.querySelectorAll('.step-item').forEach(step => {
    step.addEventListener('click', () => {
        const stepNum = step.dataset.step;

        // Update active
        document.querySelectorAll('.step-item').forEach(s => {
            s.classList.remove('active');
            if (parseInt(s.dataset.step) <= parseInt(stepNum)) {
                s.classList.add('completed');
            }
        });
        step.classList.add('active');
        step.classList.remove('completed');

        // Show content
        document.querySelectorAll('.step-content').forEach(c => {
            c.classList.toggle('hidden', c.dataset.step !== stepNum);
        });
    });
});

// Utilities
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Toast
function showToast(message) {
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toast-message');
    toastMessage.textContent = message;
    toast.classList.add('toast-show');
    setTimeout(() => toast.classList.remove('toast-show'), 3000);
}
