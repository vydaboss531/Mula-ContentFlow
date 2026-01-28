"use client";

import { useState } from "react";

export default function Home() {
    const [url, setUrl] = useState("");
    const [format, setFormat] = useState("blog");
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<any>(null);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setResult(null);

        try {
            const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
            const res = await fetch(`${apiUrl}/process`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ url: url, format_type: format }),
            });
            const data = await res.json();
            setResult(data);
        } catch (err) {
            alert("Error generating content. Is the agent running?");
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="min-h-screen bg-black text-white selection:bg-purple-500 selection:text-white">
            {/* Background Gradients */}
            <div className="fixed inset-0 z-0 opacity-20 pointer-events-none">
                <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-purple-600 rounded-full blur-[100px]" />
                <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-blue-600 rounded-full blur-[100px]" />
            </div>

            <div className="relative z-10 max-w-5xl mx-auto px-6 py-20 flex flex-col items-center">
                {/* Header */}
                <h1 className="text-6xl font-black tracking-tighter mb-4 text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400">
                    ContentFlow
                </h1>
                <p className="text-xl text-gray-400 mb-12 text-center max-w-2xl">
                    Turn any YouTube video into a viral blog post, tweet thread, or LinkedIn article instantly with AI.
                </p>

                {/* Form Card */}
                <div className="w-full max-w-2xl p-8 rounded-3xl bg-white/5 border border-white/10 backdrop-blur-xl shadow-2xl transition-all hover:border-white/20">
                    <form onSubmit={handleSubmit} className="flex flex-col gap-6">
                        <div className="space-y-2">
                            <label className="text-sm font-medium text-gray-300 ml-1">YouTube URL</label>
                            <input
                                type="url"
                                required
                                placeholder="https://youtube.com/watch?v=..."
                                className="w-full bg-black/50 border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all font-mono text-sm"
                                value={url}
                                onChange={(e) => setUrl(e.target.value)}
                            />
                        </div>

                        <div className="space-y-2">
                            <label className="text-sm font-medium text-gray-300 ml-1">Output Format</label>
                            <div className="grid grid-cols-3 gap-3">
                                {["blog", "tweet", "linkedin"].map((f) => (
                                    <button
                                        key={f}
                                        type="button"
                                        onClick={() => setFormat(f)}
                                        className={`px-4 py-3 rounded-xl border font-medium transition-all ${format === f
                                            ? "bg-white text-black border-white"
                                            : "bg-black/20 border-white/10 text-gray-400 hover:bg-white/5"
                                            }`}
                                    >
                                        {f.charAt(0).toUpperCase() + f.slice(1)}
                                    </button>
                                ))}
                            </div>
                        </div>

                        <button
                            type="submit"
                            disabled={loading}
                            className="mt-4 w-full bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-500 hover:to-blue-500 text-white font-bold py-4 rounded-xl transition-all transform hover:scale-[1.02] active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-purple-500/25"
                        >
                            {loading ? (
                                <span className="flex items-center justify-center gap-2">
                                    <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                                    Processing Video...
                                </span>
                            ) : (
                                "Generate Content"
                            )}
                        </button>
                    </form>
                </div>

                {/* Subscription Upsell */}
                <div className="mt-8 text-center">
                    <p className="text-gray-400 text-sm mb-4">Want unlimited generations & faster speeds?</p>
                    <button
                        type="button"
                        onClick={async () => {
                            try {
                                const res = await fetch("/api/checkout", {
                                    method: "POST",
                                    headers: { "Content-Type": "application/json" },
                                    body: JSON.stringify({ priceId: process.env.NEXT_PUBLIC_STRIPE_PRICE_ID }),
                                });
                                const { sessionId } = await res.json();
                                if (sessionId) {
                                    alert(`Redirecting to Stripe Checkout with Session: ${sessionId}`);
                                }
                            } catch (err) {
                                alert("Error starting checkout");
                            }
                        }}
                        className="bg-white/10 hover:bg-white/20 text-white px-6 py-2 rounded-full text-sm font-medium border border-white/10 transition-colors"
                    >
                        Upgrade to Pro ($29/mo)
                    </button>
                </div>

                {/* Results Area */}
                {result && (
                    <div className="w-full max-w-4xl mt-16 animate-in fade-in slide-in-from-bottom-8 duration-700">
                        <div className="flex items-center gap-4 mb-6">
                            <div className="h-px bg-white/10 flex-grow" />
                            <span className="text-gray-500 uppercase text-xs tracking-widest font-bold">Generated Result</span>
                            <div className="h-px bg-white/10 flex-grow" />
                        </div>

                        <div className="bg-white/5 border border-white/10 rounded-2xl p-8 backdrop-blur-md">
                            <div className="flex items-baseline justify-between mb-4">
                                <h2 className="text-2xl font-bold text-white mb-2">{result.video.title}</h2>
                                <span className="text-xs font-mono text-green-400 px-2 py-1 rounded bg-green-400/10 border border-green-400/20">SUCCESS</span>
                            </div>

                            <p className="text-gray-400 text-sm mb-6 pb-6 border-b border-white/10 line-clamp-2">
                                {result.video.description}
                            </p>

                            <div className="prose prose-invert max-w-none">
                                <textarea
                                    className="w-full h-96 bg-black/30 text-gray-300 font-mono text-sm p-4 rounded-xl border border-white/10 focus:outline-none"
                                    readOnly
                                    value={result.generated_content}
                                />
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </main>
    );
}
