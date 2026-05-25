require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { Resend } = require('resend');

const app = express();
const port = process.env.PORT || 3000;

// Initialize Resend
const resend = new Resend(process.env.RESEND_API_KEY);

// Middleware
app.use(cors());
app.use(express.json());

app.post('/api/order', async (req, res) => {
    try {
        const { customer, cart, totals } = req.body;

        // Validation
        if (!customer || !cart || cart.length === 0) {
            return res.status(400).json({ error: 'Missing required order information' });
        }

        // Format cart items for email
        const cartHtml = cart.map(item => {
            const imgUrl = item.image || 'https://i.imgur.com/BSt2lzH.png';
            return `
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #ddd; vertical-align: middle;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <img src="${imgUrl}" alt="${item.name}" width="60" height="60" style="object-fit: cover; border-radius: 6px; border: 1px solid #eee;">
                        <span>${item.name}</span>
                    </div>
                </td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd; text-align: center; vertical-align: middle;">${item.qty}</td>
                <td style="padding: 10px; border-bottom: 1px solid #ddd; text-align: right; vertical-align: middle;">৳${(item.price * item.qty).toLocaleString()}</td>
            </tr>
            `;
        }).join('');

        // Construct HTML email content
        const htmlContent = `
            <h2>New Order Received!</h2>
            
            <h3>Customer Details</h3>
            <p><strong>Name:</strong> ${customer.name}</p>
            <p><strong>Phone:</strong> ${customer.phone}</p>
            <p><strong>Street:</strong> ${customer.street}</p>
            <p><strong>City/Town:</strong> ${customer.city}</p>
            <p><strong>District:</strong> ${customer.district}</p>
            <p><strong>ZIP/Postcode:</strong> ${customer.zip || 'N/A'}</p>
            <p><strong>Notes:</strong> ${customer.notes || 'None'}</p>

            <br/>

            <h3>Order Summary</h3>
            <table style="width: 100%; border-collapse: collapse; max-width: 600px;">
                <thead>
                    <tr style="background-color: #f4f4f4;">
                        <th style="padding: 10px; text-align: left; border-bottom: 2px solid #ddd;">Product</th>
                        <th style="padding: 10px; text-align: center; border-bottom: 2px solid #ddd;">Qty</th>
                        <th style="padding: 10px; text-align: right; border-bottom: 2px solid #ddd;">Total</th>
                    </tr>
                </thead>
                <tbody>
                    ${cartHtml}
                </tbody>
                <tfoot>
                    <tr>
                        <td colspan="2" style="padding: 10px; text-align: right; font-weight: bold;">Subtotal:</td>
                        <td style="padding: 10px; text-align: right;">৳${totals.subtotal.toLocaleString()}</td>
                    </tr>
                    <tr>
                        <td colspan="2" style="padding: 10px; text-align: right; font-weight: bold;">Shipping:</td>
                        <td style="padding: 10px; text-align: right;">৳${totals.shipping.toLocaleString()}</td>
                    </tr>
                    <tr>
                        <td colspan="2" style="padding: 10px; text-align: right; font-weight: bold; font-size: 1.1em; border-top: 2px solid #000;">Grand Total:</td>
                        <td style="padding: 10px; text-align: right; font-weight: bold; font-size: 1.1em; border-top: 2px solid #000;">৳${totals.grandTotal.toLocaleString()}</td>
                    </tr>
                </tfoot>
            </table>
            
            <br/>
            <p><strong>Payment Method:</strong> Cash on Delivery</p>
        `;

        const notificationEmail = process.env.NOTIFICATION_EMAIL || 'your_email@example.com';

        // Send email via Resend
        // Using 'onboarding@resend.dev' as sender which is Resend's default testing email
        const data = await resend.emails.send({
            from: 'Food Lab Orders <onboarding@resend.dev>',
            to: [notificationEmail],
            subject: `New Order from ${customer.name} - ৳${totals.grandTotal.toLocaleString()}`,
            html: htmlContent
        });

        if (data.error) {
            console.error('Resend API Error:', data.error.message);
        } else {
            console.log('Order notification email sent successfully!');
        }

        res.status(200).json({ success: true, data });
    } catch (error) {
        console.error('Error sending email:', error);
        res.status(500).json({ error: 'Failed to process order notification' });
    }
});

app.listen(port, () => {
    console.log(`Backend server running at http://localhost:${port}`);
});
