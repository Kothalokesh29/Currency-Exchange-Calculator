import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="Global Currency Converter",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Global Currency Converter")

# Country and Currency Mapping
country_currency = {
    "🇮🇳 India": "INR",
    "🇺🇸 United States": "USD",
    "🇬🇧 United Kingdom": "GBP",
    "🇪🇺 European Union": "EUR",
    "🇯🇵 Japan": "JPY",
    "🇦🇪 United Arab Emirates": "AED",
    "🇨🇦 Canada": "CAD",
    "🇦🇺 Australia": "AUD",
    "🇨🇳 China": "CNY",
    "🇸🇬 Singapore": "SGD",
    "🇳🇿 New Zealand": "NZD",
    "🇨🇭 Switzerland": "CHF",
    "🇸🇦 Saudi Arabia": "SAR",
    "🇶🇦 Qatar": "QAR",
    "🇰🇼 Kuwait": "KWD",
    "🇧🇭 Bahrain": "BHD",
    "🇴🇲 Oman": "OMR",
    "🇿🇦 South Africa": "ZAR",
    "🇰🇷 South Korea": "KRW",
    "🇹🇭 Thailand": "THB",
    "🇲🇾 Malaysia": "MYR",
    "🇮🇩 Indonesia": "IDR",
    "🇵🇭 Philippines": "PHP",
    "🇻🇳 Vietnam": "VND",
    "🇵🇰 Pakistan": "PKR",
    "🇧🇩 Bangladesh": "BDT",
    "🇱🇰 Sri Lanka": "LKR",
    "🇳🇵 Nepal": "NPR",
    "🇷🇺 Russia": "RUB",
    "🇹🇷 Turkey": "TRY",
    "🇵🇱 Poland": "PLN",
    "🇨🇿 Czech Republic": "CZK",
    "🇭🇺 Hungary": "HUF",
    "🇷🇴 Romania": "RON",
    "🇧🇷 Brazil": "BRL",
    "🇲🇽 Mexico": "MXN",
    "🇦🇷 Argentina": "ARS",
    "🇨🇱 Chile": "CLP",
    "🇨🇴 Colombia": "COP",
    "🇪🇬 Egypt": "EGP",
    "🇳🇬 Nigeria": "NGN",
    "🇰🇪 Kenya": "KES",
    "🇬🇭 Ghana": "GHS",
    "🇮🇱 Israel": "ILS"
}

# Amount Input
amount = st.number_input(
    "💰 Enter Amount",
    min_value=1.0,
    value=1000.0
)

# Country Selection
col1, col2 = st.columns(2)

with col1:
    from_country = st.selectbox(
        "From Country",
        list(country_currency.keys())
    )

with col2:
    to_country = st.selectbox(
        "To Country",
        list(country_currency.keys())
    )

# Get Currency Codes
from_currency = country_currency[from_country]
to_currency = country_currency[to_country]

# Convert Button
if st.button("🔄 Convert Currency"):

    try:
        url = f"https://open.er-api.com/v6/latest/{from_currency}"

        response = requests.get(url)

        data = response.json()

        rate = data["rates"][to_currency]

        converted_amount = amount * rate

        st.success(
            f"{amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}"
        )

        st.info(
            f"Current Exchange Rate: 1 {from_currency} = {rate:.6f} {to_currency}"
        )

        st.write(
            f"🕒 Last Updated: {data['time_last_update_utc']}"
        )

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("🌍 Real-Time Currency Converter using Exchange Rate API")