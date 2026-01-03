# ⚛️ React Frontend Documentation

## Complete React Implementation Details

This document provides a comprehensive overview of the React frontend implementation.

---

## 📁 Frontend File Structure

```
frontend/
├── package.json          # React dependencies and scripts
├── public/
│   └── index.html       # Main HTML with Google Fonts (Unbounded, Instrument Sans)
└── src/
    ├── index.js         # React app entry point
    ├── index.css        # Base CSS styles
    ├── App.js           # Main React component (ALL UI LOGIC)
    └── App.css          # Complete styling (500+ lines)
```

---

## 📦 Dependencies (package.json)

```json
{
  "name": "system-design-visualizer-frontend",
  "version": "1.0.0",
  "dependencies": {
    "react": "^18.2.0",           // React library
    "react-dom": "^18.2.0",       // React DOM renderer
    "react-scripts": "5.0.1",     // Create React App scripts
    "axios": "^1.6.2"             // HTTP client for API calls
  }
}
```

### What Each Package Does:
- **react**: Core React library for building UI
- **react-dom**: Renders React components to browser DOM
- **react-scripts**: Build tools (webpack, babel, etc.)
- **axios**: Makes HTTP requests to Flask backend

---

## 🎨 App.js - Main Component (270+ lines)

### Component Structure

```javascript
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  // STATE MANAGEMENT
  // FORM DATA
  // API CALLS
  // UI RENDERING
}
```

### 1️⃣ State Management (useState)

```javascript
const [formData, setFormData] = useState({
  topic: 'uber',           // Selected system
  design: 'hld',           // HLD or LLD
  ai_provider: 'gemini',   // AI provider choice
  generate_gif: false      // GIF generation flag
});

const [loading, setLoading] = useState(false);    // Loading state
const [result, setResult] = useState(null);       // API response
const [error, setError] = useState(null);         // Error messages
```

### 2️⃣ Data Configuration

#### Topics Array (8 Systems)
```javascript
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
```

#### Design Types Array
```javascript
const designTypes = [
  { 
    value: 'hld', 
    label: 'High Level Design', 
    desc: 'Overall system architecture' 
  },
  { 
    value: 'lld', 
    label: 'Low Level Design', 
    desc: 'Detailed component design' 
  }
];
```

#### AI Providers Array
```javascript
const aiProviders = [
  { value: 'gemini', label: 'Google Gemini', icon: '✨' },
  { value: 'cohere', label: 'Cohere', icon: '🧠' },
  { value: 'huggingface', label: 'HuggingFace', icon: '🤗' }
];
```

### 3️⃣ Form Submission Handler

```javascript
const handleSubmit = async (e) => {
  e.preventDefault();              // Prevent page reload
  setLoading(true);                // Show loading spinner
  setError(null);                  // Clear previous errors
  setResult(null);                 // Clear previous results

  try {
    // POST request to Flask backend
    const response = await axios.post(
      'http://localhost:5000/api/generate', 
      formData
    );
    
    if (response.data.success) {
      setResult(response.data);    // Store successful result
    } else {
      setError(response.data.error); // Store error message
    }
  } catch (err) {
    // Handle network errors
    setError(err.response?.data?.error || err.message);
  } finally {
    setLoading(false);             // Hide loading spinner
  }
};
```

### 4️⃣ UI Components

#### Header Section
```jsx
<header className="header">
  <div className="logo">
    <span className="logo-icon">⚡</span>
    <h1>SysDiagram</h1>
  </div>
  <p className="tagline">AI-Powered System Architecture Visualizer</p>
</header>
```

#### Topic Selection Grid
```jsx
<div className="topic-grid">
  {topics.map((topic) => (
    <button
      key={topic.value}
      className={`topic-button ${formData.topic === topic.value ? 'active' : ''}`}
      onClick={() => setFormData({ ...formData, topic: topic.value })}
    >
      <span className="topic-icon">{topic.icon}</span>
      <span className="topic-label">{topic.label}</span>
    </button>
  ))}
</div>
```

#### Design Type Radio Buttons
```jsx
<div className="design-options">
  {designTypes.map((design) => (
    <label className={`design-option ${formData.design === design.value ? 'active' : ''}`}>
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
```

#### AI Provider Selector
```jsx
<div className="provider-select">
  {aiProviders.map((provider) => (
    <button
      type="button"
      className={`provider-button ${formData.ai_provider === provider.value ? 'active' : ''}`}
      onClick={() => setFormData({ ...formData, ai_provider: provider.value })}
    >
      <span className="provider-icon">{provider.icon}</span>
      <span className="provider-label">{provider.label}</span>
    </button>
  ))}
</div>
```

#### Submit Button with Loading State
```jsx
<button type="submit" className="submit-button" disabled={loading}>
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
```

#### Error Display
```jsx
{error && (
  <div className="error-card">
    <span className="error-icon">⚠️</span>
    <div className="error-content">
      <h3>Generation Failed</h3>
      <p>{error}</p>
    </div>
  </div>
)}
```

#### Result Display with Images
```jsx
{result && (
  <div className="result-card">
    <h2>
      <span className="result-icon">🎨</span>
      Your Architecture Diagram
    </h2>
    
    {/* PNG Image */}
    <div className="image-container">
      <img 
        src={`http://localhost:5000${result.image_path}`}
        alt="Architecture Diagram"
      />
      <a 
        href={`http://localhost:5000${result.image_path}`}
        download="architecture.png"
        className="download-button"
      >
        📥 Download PNG
      </a>
    </div>

    {/* GIF Image (if generated) */}
    {result.gif_path && (
      <div className="image-container">
        <img src={`http://localhost:5000${result.gif_path}`} />
        <a 
          href={`http://localhost:5000${result.gif_path}`}
          download="architecture.gif"
        >
          📥 Download GIF
        </a>
      </div>
    )}

    {/* Components Display */}
    <h3>Extracted Components</h3>
    <div className="component-tags">
      {result.components.map((comp, idx) => (
        <span key={idx} className="component-tag">{comp}</span>
      ))}
    </div>

    {/* Relationships Display */}
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
)}
```

---

## 🎨 App.css - Complete Styling (500+ lines)

### Design System

#### Color Palette
```css
/* Background */
--bg-primary: #0a0e1a;           /* Dark blue-black */
--bg-secondary: rgba(15, 20, 35, 0.9);  /* Card backgrounds */

/* Accent Colors */
--cyan: #00ffff;                 /* Cyan highlights */
--magenta: #ff00ff;              /* Magenta accents */
--purple: rgba(138, 43, 226, 0.3); /* Purple gradients */
--pink: rgba(255, 20, 147, 0.3);   /* Pink gradients */
```

#### Typography
```css
/* Fonts */
font-family: 'Unbounded', sans-serif;      /* Headings - Bold, geometric */
font-family: 'Instrument Sans', sans-serif; /* Body - Clean, modern */
```

### Key CSS Features

#### 1. Animated Background
```css
.background-grid {
  background-image: linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 50px 50px;
  animation: gradientShift 20s ease infinite;
}
```

#### 2. Topic Grid Layout
```css
.topic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 12px;
}
```

#### 3. Button Hover Effects
```css
.topic-button:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(0, 255, 255, 0.4);
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 255, 255, 0.2);
}
```

#### 4. Loading Spinner
```css
.spinner {
  width: 18px;
  height: 18px;
  border: 3px solid rgba(0, 0, 0, 0.3);
  border-top-color: #000;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

#### 5. Fade In Animations
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

#### 6. Responsive Design
```css
@media (max-width: 768px) {
  .topic-grid {
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  }
  
  .design-options {
    grid-template-columns: 1fr;
  }
}
```

---

## 🔄 Data Flow

### Request Flow
```
User clicks "Generate" 
    ↓
handleSubmit() called
    ↓
setLoading(true) → Show spinner
    ↓
axios.post() to backend
    ↓
Wait for response
    ↓
Success: setResult(data) → Display images
    ↓
Error: setError(msg) → Display error
    ↓
setLoading(false) → Hide spinner
```

### State Updates Flow
```
Initial State:
  formData = { topic: 'uber', design: 'hld', ... }
  loading = false
  result = null
  error = null

User selects Netflix:
  onClick → setFormData({ ...formData, topic: 'netflix' })
  Re-render with new selection

User clicks Generate:
  handleSubmit() → setLoading(true)
  Re-render with spinner

Backend responds:
  setResult(data) + setLoading(false)
  Re-render with images and data
```

---

## 🚀 Running the Frontend

### Development Mode
```bash
cd frontend
npm start
```

This starts:
- Development server on port 3000
- Hot reloading (auto-refresh on code changes)
- Error overlay for debugging

### Production Build
```bash
cd frontend
npm run build
```

Creates optimized production build in `frontend/build/`

---

## 🧪 Testing the UI

### Manual Testing Checklist

1. **Topic Selection**
   - [ ] Click each system
   - [ ] Active state shows correctly
   - [ ] Can switch between systems

2. **Design Type**
   - [ ] Select HLD
   - [ ] Select LLD
   - [ ] Only one selected at a time

3. **AI Provider**
   - [ ] Select each provider
   - [ ] Active state highlights

4. **Form Submission**
   - [ ] Click Generate
   - [ ] Spinner appears
   - [ ] Button disabled during loading

5. **Results Display**
   - [ ] Image appears
   - [ ] Download button works
   - [ ] Components list shows
   - [ ] Relationships display

6. **Error Handling**
   - [ ] Error message shows on failure
   - [ ] Can retry after error

---

## 🎯 Key React Concepts Used

### 1. **Hooks**
- `useState`: Managing component state
- State updates trigger re-renders

### 2. **Conditional Rendering**
```javascript
{loading && <Spinner />}
{error && <ErrorMessage />}
{result && <ResultDisplay />}
```

### 3. **Event Handling**
- `onClick`: Button clicks
- `onChange`: Input changes
- `onSubmit`: Form submission

### 4. **Array Mapping**
```javascript
{topics.map((topic) => <Button key={topic.value} />)}
```

### 5. **CSS Modules**
- Scoped styles via className
- No style conflicts

### 6. **Async/Await**
- Modern async handling
- Clean error handling with try/catch

---

## 📚 Learning Resources

### React Documentation
- Official Docs: https://react.dev
- Hooks Guide: https://react.dev/reference/react/hooks

### Axios Documentation
- Official Docs: https://axios-http.com

### CSS Animations
- MDN Web Docs: https://developer.mozilla.org/en-US/docs/Web/CSS/animation

---

## ✅ Summary

The React frontend includes:

✅ **Complete UI Implementation** (270+ lines)
✅ **State Management** with useState
✅ **API Integration** with axios
✅ **Modern CSS** (500+ lines with animations)
✅ **Responsive Design** (mobile-friendly)
✅ **Error Handling** (user-friendly messages)
✅ **Loading States** (spinners and indicators)
✅ **Download Functionality** (PNG and GIF)
✅ **Component Display** (extracted data visualization)

**All React code is included and ready to run!** 🚀

---

**Next Steps:**
1. Run `npm install` in frontend directory
2. Run `npm start` to launch development server
3. Open http://localhost:3000
4. Start building diagrams!
