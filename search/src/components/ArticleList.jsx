export default function ArticleList({ articles, onSelect }) {
return (
<div>
{articles.map((a) => (
<div key={a.id} style={{ border: '1px solid #ccc', margin: '5px', padding: '10px' }}>
<h3>{a.title}</h3>
<p>{a.abstract}</p>
<button onClick={() => onSelect(a.id)}>Посмотреть</button>
</div>
))}
</div>
);
}