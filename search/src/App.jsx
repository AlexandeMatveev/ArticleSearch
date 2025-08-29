import React, { useState } from "react";
import SearchForm from "./components/SearchForm";
import ArticleList from "./components/ArticleList";
import ArticleDetail from "./components/ArticleDetail"; // пока можно не использовать
import "./App.css";

function App() {
  const [articles] = useState([
    { id: 1, title: "Название статьи 1", abstract: "Краткое описание / abstract..." },
    { id: 2, title: "Название статьи 2", abstract: "Краткое описание / abstract..." },
    { id: 3, title: "Название статьи 3", abstract: "Краткое описание / abstract..." },
  ]);

  return (
    <div className="app-container">
      <h1 className="title">Research App</h1>
      <button className="upload-btn">Загрузить PDF</button>

      <SearchForm />

      <div className="results">
        <h2 className="subtitle">Результаты поиска:</h2>
        <ArticleList articles={articles} />
      </div>

      <div className="graph">
        <h2 className="subtitle">Граф статей</h2>
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/320px-6n-graf.svg.png"
          alt="graph"
          className="graph-img"
        />
      </div>
    </div>
  );
}

export default App;
