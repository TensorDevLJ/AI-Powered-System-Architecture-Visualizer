import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:5000';

function App() {
  const [formData, setFormData] = useState({
    topic: 'uber',
    design: 'hld',
    ai_provider: 'gemini',
    generate_gif: false
  });
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const topics = [
    { value: 'uber', label: 'Uber', icon: '🚗' },
    { value: 'amazon', label: 'Amazon', icon: '📦' },
    { value: 'netflix', label: 'Netflix', icon: '🎬' },
    { value: 'whatsapp', label: 'WhatsApp', icon: '💬' },
    { value: 'instagram', label: 'Instagram', icon: '📸' },
    { value: 'twitter', label: 'Twitter', icon: '🐦' },
    { value: 'youtube', label: 'YouTube', icon: '📺' },
    { value: 'dns', label: 'DNS', icon: '🌐' }
  ];

  const designTypes = [
    { value: 'hld', label: 'High Level Design', desc: 'Overall system architecture' },
    { value: 'lld', label: 'Low Level Design', desc: 'Detailed component design' }
  ];

  const aiProviders = [
    { value: 'gemini', label: 'Google Gemini', icon: '✨' },
    { value: 'cohere', label: 'Cohere', icon: '🧠' },
    { value: 'huggingface', label: 'HuggingFace', icon: '🤗' }
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post(`${API_URL}/api/generate`, formData);
      
      if (response.data.success) {
        setResult(response.data);
      } else {
        setError(response.data.error || 'Generation failed');
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message || 'Network error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="background-grid"></div>
      <div className="background-gradient"></div>
      
      <header className="header">
        <div className="logo">
          <span className="logo-icon">⚡</span>
          <h1>SysDiagram</h1>
        </div>
        <p className="tagline">AI-Powered System Architecture Visualizer</p>
      </header>

      <main className="main-content">
        <div className="container">
          <form onSubmit={handleSubmit} className="form-card">
            <div className="form-section">
              <label className="section-label">
                <span className="label-icon">🎯</span>
                Select System
              </label>
              <div className="topic-grid">
                {topics.map((topic) => (
                  <button
                    key={topic.value}
                    type="button"
                    className={`topic-button ${formData.topic === topic.value ? 'active' : ''}`}
                    onClick={() => setFormData({ ...formData, topic: topic.value })}
                  >
                    <span className="topic-icon">{topic.icon}</span>
                    <span className="topic-label">{topic.label}</span>
                  </button>
                ))}
              </div>
            </div>

            <div className="form-section">
              <label className="section-label">
                <span className="label-icon">📐</span>
                Design Type
              </label>
              <div className="design-options">
                {designTypes.map((design) => (
                  <label
                    key={design.value}
                    className={`design-option ${formData.design === design.value ? 'active' : ''}`}
                  >
                    <input
                      type="radio"
                      name="design"
                      value={design.value}
                      checked={formData.design === design.value}
                      onChange={(e) => setFormData({ ...formData, design: e.target.value })}
                    />
                    <div className="design-content">
                      <span className="design-label">{design.label}</span>
                      <span className="design-desc">{design.desc}</span>
                    </div>
                  </label>
                ))}
              </div>
            </div>

            <div className="form-section">
              <label className="section-label">
                <span className="label-icon">🤖</span>
                AI Provider
              </label>
              <div className="provider-select">
                {aiProviders.map((provider) => (
                  <button
                    key={provider.value}
                    type="button"
                    className={`provider-button ${formData.ai_provider === provider.value ? 'active' : ''}`}
                    onClick={() => setFormData({ ...formData, ai_provider: provider.value })}
                  >
                    <span className="provider-icon">{provider.icon}</span>
                    <span className="provider-label">{provider.label}</span>
                  </button>
                ))}
              </div>
            </div>

            <div className="form-section">
              <label className="checkbox-label">
                <input
                  type="checkbox"
                  checked={formData.generate_gif}
                  onChange={(e) => setFormData({ ...formData, generate_gif: e.target.checked })}
                />
                <span className="checkbox-text">
                  <span className="checkbox-icon">🎞️</span>
                  Generate animated GIF
                </span>
              </label>
            </div>

            <button
              type="submit"
              className="submit-button"
              disabled={loading}
            >
              {loading ? (
                <>
                  <span className="spinner"></span>
                  Generating Architecture...
                </>
              ) : (
                <>
                  <span className="button-icon">✨</span>
                  Generate Diagram
                </>
              )}
            </button>
          </form>

          {error && (
            <div className="error-card">
              <span className="error-icon">⚠️</span>
              <div className="error-content">
                <h3>Generation Failed</h3>
                <p>{error}</p>
              </div>
            </div>
          )}

          {result && (
            <div className="result-card">
              <div className="result-header">
                <h2>
                  <span className="result-icon">🎨</span>
                  Your Architecture Diagram
                </h2>
              </div>

              <div className="result-images">
                <div className="image-container">
                  <img
                    src={`${API_URL}${result.image_path}`}
                    alt="Architecture Diagram"
                    className="diagram-image"
                  />
                  <a
                    href={`${API_URL}${result.image_path}`}
                    download="architecture.png"
                    className="download-button"
                  >
                    <span>📥</span>
                    Download PNG
                  </a>
                </div>

                {result.gif_path && (
                  <div className="image-container">
                    <img
                      src={`${API_URL}${result.gif_path}`}
                      alt="Animated Architecture"
                      className="diagram-image"
                    />
                    <a
                      href={`${API_URL}${result.gif_path}`}
                      download="architecture.gif"
                      className="download-button"
                    >
                      <span>📥</span>
                      Download GIF
                    </a>
                  </div>
                )}
              </div>

              <div className="result-details">
                <h3>Extracted Components</h3>
                <div className="component-tags">
                  {result.components.map((comp, idx) => (
                    <span key={idx} className="component-tag">
                      {comp}
                    </span>
                  ))}
                </div>

                <h3>Relationships</h3>
                <div className="relationships-list">
                  {result.relationships.map((rel, idx) => (
                    <div key={idx} className="relationship-item">
                      <span className="rel-from">{rel.from}</span>
                      <span className="rel-arrow">→</span>
                      <span className="rel-to">{rel.to}</span>
                      <span className="rel-type">{rel.type}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>
      </main>

      <footer className="footer">
        <p>Built with React + Flask + AI • System Design Visualizer</p>
      </footer>
    </div>
  );
}

export default App;
