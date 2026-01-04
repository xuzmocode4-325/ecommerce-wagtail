##############################################
# Stage 1: Node Build (only used in production)
##############################################
FROM node:20-alpine AS build
WORKDIR /frontend

ARG DEV=false
COPY ../frontend/package*.json ./
RUN npm ci
COPY ../frontend .

RUN if [ "$DEV" != "true" ]; then \
        echo "Building production frontend..."; \
        npm run build; \
    else \
        echo "Skipping build (DEV mode)"; \
    fi

##############################################
# Stage 2: Nginx Proxy (used in both modes)
##############################################
FROM nginx:alpine
ARG DEV=false
ENV DEV=${DEV}

COPY ./proxy/nginx.conf /etc/nginx/conf.d/default.conf

# Copy built frontend if it exists
COPY --from=build /frontend/dist* /usr/share/nginx/html 

# Show placeholder HTML in dev mode
RUN if [ "$DEV" = "true" ]; then \
        echo "Running in DEV mode (proxy only)" && \
        rm -rf /usr/share/nginx/html/* && \
        echo '<h1>Proxy Container (DEV Mode)</h1><p>Frontend runs at http://localhost:5173</p>' > /usr/share/nginx/html/index.html; \
    fi

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
