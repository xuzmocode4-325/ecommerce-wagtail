<template>
  <div class="relative bg-gray-800 px-6 py-32 sm:px-12 sm:py-40 lg:px-16">
    <div class="absolute inset-0 overflow-hidden">
      <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-03-feature-section-full-width.jpg" alt="" class="size-full object-cover" />
    </div>
    <div aria-hidden="true" class="absolute inset-0 bg-gray-900/50"></div>
    <div class="relative mx-auto flex max-w-3xl flex-col items-center text-center">
      <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">Long-term thinking</h2>
      <p class="mt-3 text-xl text-white">We're committed to responsible, sustainable, and ethical manufacturing. Our small-scale approach allows us to focus on quality and reduce our impact. We're doing our best to delay the inevitable heat-death of the universe.</p>
      <a href="#" class="mt-8 block w-full rounded-md border border-transparent bg-white px-8 py-3 text-base font-medium text-gray-900 hover:bg-gray-100 sm:w-auto">Read our story</a>
    </div>
    
  </div>
  <div class="bg-white">
    <div class="py-16 sm:py-24 lg:mx-auto lg:max-w-7xl lg:px-8">
      <div class="flex items-center justify-between px-4 sm:px-6 lg:px-0">
        <h2 class="text-2xl font-bold tracking-tight text-gray-900">Trending products</h2>
        <a href="#" class="hidden text-sm font-semibold text-indigo-600 hover:text-indigo-500 sm:block">
          See everything
          <span aria-hidden="true"> &rarr;</span>
        </a>
      </div>

      <div class="relative mt-8">
        <div class="relative -mb-6 w-full overflow-x-auto pb-6">
          <ul role="list" class="mx-4 inline-flex space-x-8 sm:mx-6 lg:mx-0 lg:grid lg:grid-cols-4 lg:gap-x-8 lg:space-x-0">
            <li v-for="product in products" :key="product.id" class="inline-flex w-64 flex-col text-center lg:w-auto">
              <div class="group relative">
                <img :src="product.imageSrc" :alt="product.imageAlt" class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75" />
                <div class="mt-6">
                  <p class="text-sm text-gray-500">{{ product.color }}</p>
                  <h3 class="mt-1 font-semibold text-gray-900">
                    <a :href="product.href">
                      <span class="absolute inset-0"></span>
                      {{ product.name }}
                    </a>
                  </h3>
                  <p class="mt-1 text-gray-900">{{ product.price }}</p>
                </div>
              </div>

              <h4 class="sr-only">Available colors</h4>
              <ul role="list" class="mt-auto flex items-center justify-center space-x-3 pt-6">
                <li v-for="color in product.availableColors" :key="color.name" class="size-4 rounded-full border border-black/10" :style="{ backgroundColor: color.colorBg }">
                  <span class="sr-only">{{ color.name }}</span>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>

      <div class="mt-12 flex px-4 sm:hidden">
        <a href="#" class="text-sm font-semibold text-indigo-600 hover:text-indigo-500">
          See everything
          <span aria-hidden="true"> &rarr;</span>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
const offers = [
  { name: 'Download the app', description: 'Get an exclusive $5 off code', href: '#' },
  { name: "Return when you're ready", description: '60 days of free returns', href: '#' },
  { name: 'Sign up for our newsletter', description: '15% off your first order', href: '#' },
]

const products = [
  {
    id: 1,
    name: 'Machined Pen',
    color: 'Black',
    price: '$35',
    href: '#',
    imageSrc: 'https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-02-product-01.jpg',
    imageAlt: 'Black machined steel pen with hexagonal grip and small white logo at top.',
    availableColors: [
      { name: 'Black', colorBg: '#111827' },
      { name: 'Brass', colorBg: '#FDE68A' },
      { name: 'Chrome', colorBg: '#E5E7EB' },
    ],
  },
  {
    id: 2,
    name: 'Earthen Mug',
    color: 'Matte Black',
    price: '$28',
    href: '#',
    imageSrc: 'https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-02-product-02.jpg',
    imageAlt: 'Black porcelain mug with modern square handle and natural clay accents on rim and bottom.',
    availableColors: [
      { name: 'Matte Black', colorBg: '#4B5563' },
      { name: 'Natural', colorBg: '#FEF3C7' },
    ],
  },
  {
    id: 3,
    name: 'Leatherbound Daily Journal Set',
    color: 'Natural',
    price: '$50',
    href: '#',
    imageSrc: 'https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-02-product-03.jpg',
    imageAlt: 'Natural leather journal with brass disc binding and three paper refill sets.',
    availableColors: [
      { name: 'Natural', colorBg: '#FEF3C7' },
      { name: 'Black', colorBg: '#1F2937' },
      { name: 'Brown', colorBg: '#7C2D12' },
    ],
  },
  {
    id: 4,
    name: 'Leatherbound Daily Journal',
    color: 'Black',
    price: '$50',
    href: '#',
    imageSrc: 'https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-02-product-04.jpg',
    imageAlt: 'Black leather journal with brass disc binding.',
    availableColors: [
      { name: 'Black', colorBg: '#111827' },
      { name: 'Brown', colorBg: '#7C2D12' },
      { name: 'Natural', colorBg: '#FEF3C7' },
    ],
  },
]
</script>

