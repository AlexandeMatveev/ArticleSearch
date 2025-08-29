import React, { useState } from "react";
import "./SearchForm.css";

function SearchForm() {
  const [query, setQuery] = useState("");

  const handleSearch = (e) => {
    e.preventDefault();
    console.log("Искать:", query);
  };

  return (
    <form className="search-form" onSubmit={handleSearch}>
      <label className="search-label">Введите промпт для поиска:</label>
      <div className="search-box">
        <input
          type="text"
          placeholder=""
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit">Поиск</button>
      </div>
    </form>
  );
}

export default SearchForm;
