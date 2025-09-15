import React from "react";
import "./ArticleList.css";

function ArticleList({ articles }) {
  return (
    <div className="article-list">
      {articles.map((article) => (
        <div key={article.id} className="article-item">
          <h3>{article.title}</h3>
          <p>{article.abstract}</p>
        </div>
      ))}
    </div>
  );
}

export default ArticleList;
