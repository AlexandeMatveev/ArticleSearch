export default function ArticleDetail({ article, onRecommend }) {
return (
<div style={{ border: '1px solid #000', padding: '15px' }}>
<h2>{article.title}</h2>
<p>{article.abstract}</p>
<p>Авторы: {article.authors.join(', ')}</p>
<button onClick={() => onRecommend(article.id)} style={{ marginTop: '10px' }}>
Показать похожие статьи
</button>
</div>
);
}