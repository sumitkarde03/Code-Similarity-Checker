import { useState } from "react";
import axios from "axios";

function App() {
  const [code1, setCode1] = useState("");
  const [code2, setCode2] = useState("");
  const [result, setResult] = useState(null);

  const handleCompare = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/compare", {
        code1,
        code2,
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error comparing code:", error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white p-6">
      <h1 className="text-3xl font-bold mb-6">Code Similarity Checker</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 w-full max-w-4xl">
        <textarea
          className="p-3 bg-gray-800 rounded-lg w-full h-40"
          placeholder="Enter first code snippet..."
          value={code1}
          onChange={(e) => setCode1(e.target.value)}
        />
        
        <textarea
          className="p-3 bg-gray-800 rounded-lg w-full h-40"
          placeholder="Enter second code snippet..."
          value={code2}
          onChange={(e) => setCode2(e.target.value)}
        />
      </div>

      <button
        onClick={handleCompare}
        className="mt-4 px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg"
      >
        Compare Code
      </button>

      {result && (
        <div className="mt-6 p-4 bg-gray-800 rounded-lg w-full max-w-2xl">
          <h2 className="text-xl font-semibold">Similarity Results:</h2>
          <p>Similarity: {result.similarity.toFixed(2)}%</p>
          <p>Matching Lines: {result.matches}</p>
        </div>
      )}
    </div>
  );
}

export default App;
