import { NextResponse } from "next/server";
import Stripe from "stripe";

export async function POST(req: Request) {
    if (!process.env.STRIPE_SECRET_KEY) {
        return NextResponse.json({ error: "Stripe key missing on server" }, { status: 500 });
    }

    const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
        // @ts-ignore
        apiVersion: "2023-10-16",
    });

    try {
        const { priceId } = await req.json();

        // Basic validation
        if (!priceId) {
            return NextResponse.json({ error: "Price ID is required" }, { status: 400 });
        }

        const session = await stripe.checkout.sessions.create({
            mode: "subscription",
            payment_method_types: ["card"],
            line_items: [
                {
                    price: priceId,
                    quantity: 1,
                },
            ],
            success_url: `${req.headers.get("origin")}/?success=true`,
            cancel_url: `${req.headers.get("origin")}/?canceled=true`,
        });

        return NextResponse.json({ sessionId: session.id });
    } catch (err: any) {
        console.error("Stripe Checkout Error:", err);
        return NextResponse.json({ error: err.message }, { status: 500 });
    }
}
