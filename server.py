from flask import Flask, redirect, render_template


app = Flask(__name__)


catalog = [
    {
        'name': 'GeForce RTX 3090',
        'description': 'The GeForce RTX™ 3090 is a big ferocious GPU (BFGPU) with TITAN class performance. It’s powered\
         by Ampere—NVIDIA’s 2nd gen RTX architecture—doubling down on ray tracing and AI performance with enhanced Ray \
         Tracing (RT) Cores, Tensor Cores, and new streaming multiprocessors. Plus, it features a staggering 24 GB of \
         G6X memory, all to deliver the ultimate gaming experience.',
        'preview': 'img/rtx3090-1.png',
        'picture': 'img/rtx3090-2.jpg',
        'link': 'item/0',
        'specs': [
            ['NVIDIA CUDA Cores', '10496'],
            ['Frequency with boost', '1.7 GHz'],
            ['Video Memory', '24 Gb'],
            ['Memory Type', 'GDDR6X']
        ],
        'stock': True,
        'price': '$1499.<sup>00</sup>',
        'buy': 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/'
    },
    {
        'name': 'GeForce RTX 3080',
        'description': 'The GeForce RTX™ 3080 delivers the ultra performance that gamers crave, powered by \
        Ampere—NVIDIA’s 2nd gen RTX architecture. It’s built with enhanced RT Cores and Tensor Cores, new streaming \
        multiprocessors, and superfast G6X memory for an amazing gaming experience.',
        'preview': 'img/rtx3080-1.png',
        'picture': 'img/rtx3080-2.jpg',
        'specs': [
            ['NVIDIA CUDA Cores', '8704'],
            ['Frequency with boost', '1.71 GHz'],
            ['Video Memory', '10 Gb'],
            ['Memory Type', 'GDDR6X']
        ],
        'link': 'item/1',
        'stock': True,
        'price': '$699.<sup>00</sup>',
        'buy': 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3080/'
    },
    {
        'name': 'GeForce RTX 3070',
        'description': 'The GeForce RTX™ 3070 is powered by Ampere—NVIDIA’s 2nd gen RTX architecture. Built with \
        enhanced Ray Tracing Cores and Tensor Cores, new streaming multiprocessors, and high-speed G6 memory, it gives \
        you the power you need to rip through the most demanding games.',
        'preview': 'img/rtx3070-1.png',
        'picture': 'img/rtx3070-2.jpg',
        'specs': [
            ['NVIDIA CUDA Cores', '5888'],
            ['Frequency with boost', '1.73 GHz'],
            ['Video Memory', '8 Gb'],
            ['Memory Type', 'GDDR6']
        ],
        'link': 'item/2',
        'stock': False,
        'price': '$499.<sup>00</sup>',
        'buy': 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3070/'
    },
]


@app.route('/')
def index():
    return render_template('index.html', items=catalog)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/item')
def items():
    return redirect('/')


@app.route('/item/<int:uid>')
def item(uid):
    return render_template('item.html', items=catalog, idx=uid)


if __name__ == '__main__':
    app.run()
