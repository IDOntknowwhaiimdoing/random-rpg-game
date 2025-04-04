namespace SpriteKind {
    export const button = SpriteKind.create()
    export const outofhouse1door = SpriteKind.create()
    export const inhouse1door = SpriteKind.create()
    export const sign = SpriteKind.create()
    export const chest = SpriteKind.create()
    export const piggy = SpriteKind.create()
    export const quicktext = SpriteKind.create()
    export const popup = SpriteKind.create()
}
// tilemap junk and locations for swapping to erky's house
sprites.onOverlap(SpriteKind.Player, SpriteKind.outofhouse1door, function (sprite, otherSprite) {
    if (in_house_1 == 0) {
        sprites.destroy(house1_hitbox)
        game.splash("entering erky's house")
        tiles.setCurrentTilemap(tilemap`house1`)
        sprites.destroy(piggy)
        piggy = sprites.create(assets.image`piggy`, SpriteKind.piggy)
        tiles.placeOnTile(piggy, tiles.getTileLocation(9, 15))
        house1_hitbox = sprites.create(assets.image`doorUPSIDEDOWN`, SpriteKind.inhouse1door)
        tiles.placeOnTile(house1_hitbox, tiles.getTileLocation(10, 1))
        tiles.placeOnTile(mySprite, tiles.getTileLocation(10, 2))
        tiles.placeOnTile(press_Z, tiles.getTileLocation(10, 1))
        in_house_1 = 1
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.inhouse1door, function (sprite, otherSprite) {
    if (in_house_1 == 1) {
        sprites.destroy(house1_hitbox)
        game.splash("leaving erky's house")
        tiles.setCurrentTilemap(tilemap`world`)
        house1_hitbox = sprites.create(assets.image`doorvertical`, SpriteKind.outofhouse1door)
        tiles.placeOnTile(house1_hitbox, tiles.getTileLocation(8, 9))
        tiles.placeOnTile(mySprite, tiles.getTileLocation(8, 8))
        tiles.placeOnTile(press_Z, tiles.getTileLocation(8, 7))
        in_house_1 = 0
        sprites.destroy(piggy)
    }
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    if (inventory_open == 0) {
        music.play(music.stringPlayable("C D E F G A B C5 ", 130), music.PlaybackMode.UntilDone)
        inventory = sprites.create(assets.image`inventory`, SpriteKind.popup)
        inventory.changeScale(10, ScaleAnchor.Middle)
        inventory_open = 1
        pauseUntil(() => controller.A.isPressed())
    }
    if (inventory_open == 1) {
        music.play(music.stringPlayable("C5 B A G F E D C ", 130), music.PlaybackMode.UntilDone)
        pause(1)
        inventory_open = 0
        sprites.destroy(inventory)
        pauseUntil(() => controller.menu.isPressed())
    }
})
let money = 0
let inventory: Sprite = null
let piggy: Sprite = null
let press_Z: Sprite = null
let mySprite: Sprite = null
let house1_hitbox: Sprite = null
let in_house_1 = 0
let inventory_open = 0
inventory_open = 0
let piggys_money_stolen = 0
in_house_1 = 0
game.splash("hello")
game.splash("welcome to my rpg game")
scene.setBackgroundImage(img`
    9999999999999999bbbbbb66666666b777777777777777777777777777777777777d7669999999999999999999999999bbbbbb66666666b777777777777777777777777777777777777d766999999999
    999999999999999997bbbbbbbbbbbbb7777777777777777777777777777777777777666999999999999999999999999997bbbbbbbbbbbbb7777777777777777777777777777777777777666999999999
    99999999999999999997bbbbbbbbbbb677777777777777777777777777777777777666799999999999999999999999999997bbbbbbbbbbb6777777777777777777777777777777777776667999999999
    9999999999999999999997bbbbbbbbb66777777777777777777777777777777777666699999999999999999999999999999997bbbbbbbbb6677777777777777777777777777777777766669999999999
    9999999999999999999999999999999667777777777777777777777777777777766669999999999999999999999999999999999999999996677777777777777777777777777777777666699999999999
    9999999999999999999999999999999766777777777777777777777777777777666699999999999999999999999999999999999999999997667777777777777777777777777777776666999999999999
    9999999999999999dddd99ddddd9999966677777777777777777777777777766666999999999999999999999999999999999999999999999666777777777777777777777777777666669999999999999
    9999999999999999d11dddd1d1ddddddd66667777777777777777777777766666699999999999999999999999999999999999dddddddddddd66667777777777777777777777766666699999999999999
    9999999999999999d111dd11d11ddddddd6666666777777777777777766666667999999999999999999999999999999999dddddddddddddddd6666666777777777777777766666667999999999999999
    999999999dddd9ddd111d111d111dddd1ddddddd66666666666666666666667999999999999999999999999999999999dddddddddddddddddddd66666666666666666666666666799999999999999999
    999999999d11ddddd111d111d1111dd11dddd11d666666666666666666667999999999999999999999999999999999dddddddddddddddddddddddd666666666666666666666679999999999999999999
    999999999d111dddd1111d1111111d111ddd111dd6666666666666666799999999999999999999999999999999999dddddddddddddddddddddddddddd666666666666666679999999999999999999999
    999999999d1111dddd111d1111111111ddd1111dddddd77779999999999999999999999999999999999999999999ddddddddddddddddddddddddddddddddd77779999999999999999999999999999999
    999999999d11111ddd11111111111111dd11111ddddddd777999999999999999999999999999999999999999999ddddddddddddddddddddddddddddddddddd7779999999999999999999999999999999
    999999999d11111ddd1111111111d11ddd1111ddddddddd79999999999999999999999999999999999999999999dddddddddddddddd77777ddddddddddddddd799999999999999999999999999999999
    999999999dd11111ddd1111dd11dddddd11111ddddddddd799999999999999999b6666666667999999999999997dddddddddddddddddd7777777ddddddddddd799999999999999999b66666666679999
    9999999999d111111dd11ddd5ddddddd11111dd7dddddd7999999999999999999bb666666666667999999999997ddddddddddddddddddd7777777777dddddd7999999999999999999bb6666666666679
    79999ddd99dd111111ddd5d555dddddd1111ddd7ddddd799999999999999999997b6666666666666799999999997dddddddddddddddddddd777777777777d799999999999999999997b6666666666666
    66999d11ddddd111ddddd55555d5dddd111ddddd1111d99999999999966b7999997b6666666666666699999999977ddddddddddddddddddddd7799977777799999999999966b7999997b666666666666
    66699d1111dddd11d11dd5555555dd11d1ddddd1111dd9999999999966666679999bb6666666666666699999999977dddddddddddddddddddddd7999999999999999999966666679999bb66666666666
    666799d1111ddddddd111dd555511111ddddd11111dd9999999999966666666b9997b666666666666667999999999777ddddddddddddddddd777799999999999999999966666666b9997b66666666666
    666699dd11111ddddd11111d5d11111dddd111111dd9999999999966666666666b99bb666666666666669999999999777777777777777777777799999999999999999966666666666b99bb6666666666
    6666977ddd11111dddd11111d11111ddd11111dddd999999999996666666666666677b6666666666666697777669999977777777777777777999999999999999999996666666666666677b6666666666
    667777777dddd1111ddd11ddddd11dd1111ddddddd9999999999966666666666666666666666666666777777776999999999999999999999999999999999999999999666666666666666666666666666
    7777777111111ddddddddd11111ddddddddd111111d999999999676666666666666666666666666777777777776999999999999966799999999999999999999999996766666666666666666666666667
    77777771111111111dddd1111111dddd11111111177999999999b76666666666666666666666677777777777776799999999996677dd799999999999999ddddd99dddd66666666666666666666666777
    777777777111111dddddddd111dddddddd111117779999999999b676666666666666666666677777777777777776999999996677777d7799999999999ddd1d1dddd11d76666666666666666666677777
    77777777777777dd7d11ddddddddd111dddddd779999999999997b77666666666666666666777777777777777776799999667777777dd7999999ddd99dd11d11dd111d77666666666666666666777777
    777777777ddddd771111d111dddd11111177dddd7799999999999bb77666666666666666677777777777777777776999667777777777d7dddd99d1dddd111d111d111ddd7dddd6666666666667777777
    77777777ddddd7711111d1111ddd711111177dddd7799999999997bb7776666666666666777777777777777777776666777777777777d7d11dd9d11dd1111d111d111ddddd11d6666666666677777777
    7777777ddddd7711111dd11111dd77111111777777999999999999bbb677666666666667777777777777777777776677777777777777d7d111ddd111d1111111d1111dddd111d6666666666777777777
    777777777ddd711111d7dd1111ddd67d11111d99999999999999999bbb6666666666666777777777777777777777777777777777777dd6d1111ddd1111111111d111dddd1111d6666666666777777777
    777777777777d111dd777d11111d7669ddddd9999999999999999999bbbbbb66666666b777777777777777777777777777777777777d76d11111dd11111111111111ddd11111db66666666b777777777
    7777777777777ddd777777d1111d666999999999999999999999999997bbbbbbbbbbbbb777777777777777777777777777777777777766dd1111ddd11d1111111111ddd11111dbbbbbbbbbb777777777
    77777777777777777777777d111d66799999999999999999999999999997bbbbbbbbbbb677777777777777777777777777777777777666dd11111dddddd11dd1111ddd11111ddbbbbbbbbbb677777777
    777777777777777777777777ddd66699999999999999999999999999999997bbbbbbbbb6677777777777777777777777777777777766669dd11111ddddddd5ddd11dd111111d97bbbbbbbbb667777777
    7777777777777777777777777666699999999999999999999999999999999999999999966777777777777777777777777777777776dddd9ddd1111dddddd555d5ddd111111dd99ddd999999667777777
    777777777777777777777777666699999999999999999999999999999999999999999997667777777777777777777777777777776d1111ddddd111dddd5d55555ddddd111ddddd11d999999766777777
    777777777777777777777766666999999999999999999999999999999999999999999999666777777777777777777777777777666dd1111ddddd1d11dd5555555dd11d11dddd1111d999999966677777
    7777777777777777777766666699999999999999999999999999999999999dddddddddddd666677777777777777777777777666666dd11111ddddd111115555dd111ddddddd1111dddddddddd6666777
    6777777777777777766666667999999999999999999999999999999999dddddddddddddddd666666677777777777777776666666799dd111111dddd11111d5d11111ddddd11111dddddddddddd666666
    66666666666666666666667999999999999999999999999999999999dddddddddddddddddddd66666666666666666666666666799999dddd11111ddd11111d11111dddd11111dddddddddddddddd6666
    666666666666666666667999999999999999999999999999999999dddddddddddddddddddddddd666666666666666666666679999999ddddddd1111dd11ddddd11ddd1111dddd777dddddddddddddd66
    d6666666666666666799999999999999999999999999999999999dddddddddddddddddddddddddddd66666666666666667999999999d111111ddddddddd11111ddddddddd1111117dddddddddddddddd
    ddddd77779999999999999999999999999999999999999999999ddddddddddddddddddddddddddddddddd777799999999999999999977111111111dddd1111111dddd11111111117dddddddddddddddd
    dddddd777999999999999999999999999999999999999999999ddddddddddddddddddddddddddddddddddd777999999999999999999977711111dddddddd111dddddddd11111177ddddddddddddddddd
    ddddddd79999999999999999999999999999999999999999999dddddddddddddddd77777ddddddddddddddd7999999999999999999999977dddddd111ddddddddd11d7dd77777dddddd77777dddddddd
    ddddddd799999999999999999b6666666667999999999999997dddddddddddddddddd7777777ddddddddddd799999999999999999b6677dddd77111111dddd111d111177ddddddddddddd7777777dddd
    dddddd7999999999999999999bb666666666667999999999997ddddddddddddddddddd7777777777dddddd7999999999999999999bb77dddd771111117ddd1111d1111177ddddddddddddd7777777777
    7777d799999999999999999997b6666666666666799999999997dddddddddddddddddddd777777777777d799999999999999999997b677777711111177dd11111dd1111177dddddddddddddd77777777
    7777799999999999966b7999997b6666666666666699999999977ddddddddddddddddddddd7799977777799999999999966b7999997b6666d11111d766dd1111dd9d111117dddddddddddddddd779997
    999999999999999966666679999bb6666666666666699999999977dddddddddddddddddddddd7999999999999999999966666679999bb6666ddddd6666d11111d999dd111ddddddddddddddddddd7999
    99999999999999966666666b9997b666666666666667999999999777ddddddddddddddddd777799999999999999999966666666b9997b6666666666666d1111d999997ddddddddddddddddddd7777999
    9999999999999966666666666b99bb666666666666669999999999777777777777777777777799999999999999999966666666666b99bb666666666666d111d999999977777777777777777777779999
    99999999999996666666666666677b6666666666666697777669999977777777777777777999999999999999999996666666666666677b6666666666666ddd7776699999777777777777777779999999
    9999999999999666666666666666666666666666667777777769999999999999999999999999999999999999999996666666666666666666666666666677777777699999999999999999999999999999
    9999999999996766666666666666666666666667777777777769999999999999667999999999999999999999999967666666666666666666666666677777777777699999999999996679999999999999
    999999999999b76666666666666666666666677777777777776799999999996677dd799999999999999999999999b76666666666666666666666677777777777776799999999996677dd799999999999
    999999999999b676666666666666666666677777777777777776999999996677777d779999999999999999999999b676666666666666666666677777777777777776999999996677777d779999999999
    9999999999997b77666666666666666666777777777777777776799999667777777dd799999999999999999999997b77666666666666666666777777777777777776799999667777777dd79999999999
    9999999999999bb77666666666666666677777777777777777776999667777777777d769999999999999999999999bb77666666666666666677777777777777777776999667777777777d76999999999
    99999999999997bb7776666666666666777777777777777777776666777777777777d7699999999999999999999997bb7776666666666666777777777777777777776666777777777777d76999999999
    99999999999999bbb677666666666667777777777777777777776677777777777777d7699999999999999999999999bbb677666666666667777777777777777777776677777777777777d76999999999
    999999999999999bbb6666666666666777777777777777777777777777777777777dd66999999999999999999999999bbb6666666666666777777777777777777777777777777777777dd66999999999
    9999999999999999bbbbbb66666666b777777777777777777777777777777777777d7669999999999999999999999999bbbbbb66666666b777777777777777777777777777777777777d766999999999
    999999999999999997bbbbbbbbbbbbb7777777777777777777777777777777777777666999999999999999999999999997bbbbbbbbbbbbb7777777777777777777777777777777777777666999999999
    99999999999999999997bbbbbbbbbbb677777777777777777777777777777777777666799999999999999999999999999997bbbbbbbbbbb6777777777777777777777777777777777776667999999999
    9999999999999999999997bbbbbbbbb66777777777777777777777777777777777666699999999999999999999999999999997bbbbbbbbb6677777777777777777777777777777777766669999999999
    9999999999999999999999999999999667777777777777777777777777777777766669999999999999999999999999999999999999999996677777777777777777777777777777777666699999999999
    9999999999999999999999999999999766777777777777777777777777777777666699999999999999999999999999999999999999999997667777777777777777777777777777776666999999999999
    9999999999999999999999999999999966677777777777777777777777777766666999999999999999999999999999999999999999999999666777777777777777777777777777666669999999999999
    999999999999999999999dddddddddddd66667777777777777777777777766666699999999999999999999999999999999999dddddddddddd66667777777777777777777777766666699999999999999
    999999999999999999dddddddddddddddd6666666777777777777777766666667999999999999999999999999999999999dddddddddddddddd6666666777777777777777766666667999999999999999
    9999999999999999dddddddddddddddddddd666666666666666666666666667999999999999999999999999999999999dddddddddddddddddddd66666666666666666666666666799999999999999999
    99999999999999dddddddddddddddddddddddd66666666666666666666667999999999999999999999999999999999dddddddddddddddddddddddd666666666666666666666679999999999999999999
    9999999999999dddddddddddddddddddddddddddd6666666666666666799999999999999999999999999999999999dddddddddddddddddddddddddddd666666666666666679999999999999999999999
    999999999999ddddddddddddddddddddddddddddddddd77779999999999999999999999999999999999999999999ddddddddddddddddddddddddddddddddd77779999999999999999999999999999999
    99999999999ddddddddddddddddddddddddddddddddddd777999999999999999999999999999999999999999999ddddddddddddddddddddddddddddddddddd7779999999999999999999999999999999
    99999999999dddddddddddddddd77777ddddddddddddddd79999999999999999999999999999999999999999999dddddddddddddddd77777ddddddddddddddd799999999999999999999999999999999
    99999999997dddddddddddddddddd7777777ddddddddddd799999999999999999b6666666667999999999999997dddddddddddddddddd7777777ddddddddddd799999999999999999b66666666679999
    99999999997ddddddddddddddddddd7777777777dddddd7999999999999999999bb666666666667999999999997ddddddddddddddddddd7777777777dddddd7999999999999999999bb6666666666679
    799999999997dddddddddddddddddddd777777777777d799999999999999999997b6666666666666799999999997dddddddddddddddddddd777777777777d799999999999999999997b6666666666666
    6699999999977ddddddddddddddddddddd7799977777799999999999966b7999997b6666666666666699999999977ddddddddddddddddddddd7799977777799999999999966b7999997b666666666666
    66699999999977dddddddddddddddddddddd7999999999999999999966666679999bb6666666666666699999999977dddddddddddddddddddddd7999999999999999999966666679999bb66666666666
    6667999999999777ddddddddddddddddd777799999999999999999966666666b9997b666666666666667999999999777ddddddddddddddddd777799999999999999999966666666b9997b66666666666
    66669999999999777777777777777777777799999999999999999966666666666b99bb666666666666669999999999777777777777777777777799999999999999999966666666666b99bb6666666666
    666697777669999977777777777777777999999999999999999996666666666666677b6666666666666697777669999977777777777777777999999999999999999996666666666666677b6666666666
    6677777777699999999999999999999999999999999999999999966666666666666666666666666666777777776999999999999999999999999999999999999999999666666666666666666666666666
    7777777777699999999999996679999999dddd99ddddd9999999676666666666666666666666666777777777776999999999999966799999999999999999999999996766666666666666666666666667
    77777777776799999999996677dd799999d11dddd1d1ddd99999b76666666666666666666666677777777777776799999999996677dd799999999999999999999999b766666666666666666666666777
    777777777776999999996677777d779999d111dd11d11dd99dddb676666666666666666666677777777777777776999999996677777d779999999999999999999999b676666666666666666666677777
    777777777776799999667777777dddd9ddd111d111d111dddd1d7bdddd6666666666666666777777777777777776799999667777777dd799999999999999999999997b77666666666666666666777777
    777777777777699966777777777d11ddddd111d111d1111dd11d9dd11d66666666666666677777777777777777776999667777777777d769999999999999999999999bb7766666666666666667777777
    777777777777666677777777777d111dddd1111d1111111d111ddd111d76666666666666777777777777777777776666777777777777d7699999999999999999999997bb777666666666666677777777
    777777777777667777777777777d1111dddd111d1111111111ddd1111d77666666666667777777777777777777776677777777777777d7699999999999999999999999bbb67766666666666777777777
    777777777777777777777777777d11111ddd11111111111111dd11111d6666666666666777777777777777777777777777777777777dd66999999999999999999999999bbb6666666666666777777777
    777777777777777777777777777d11111ddd1111111111d11ddd1111ddbbbb66666666b777777777777777777777777777777777777d7669999999999999999999999999bbbbbb66666666b777777777
    777777777777777777777777777dd11111ddd1111dd11dddddd11111ddbbbbbbbbbbbbb7777777777777777777777777777777777777666999999999999999999999999997bbbbbbbbbbbbb777777777
    7777777777777777777777777776d111111dd11ddd5ddddddd11111dd997bbbbbbbbbbb677777777777777777777777777777777777666799999999999999999999999999997bbbbbbbbbbb677777777
    77777777777777777777777ddd66dd111111ddd5d555dddddd1111ddd9ddddbbbbbbbbb66777777777777777777777777777777777666699999999999999999999999999999997bbbbbbbbb667777777
    77777777777777777777777d11ddddd111ddddd55555d5dddd111ddddd1111d9999999966777777777777777777777777777777776666999999999999999999999999999999999999999999667777777
    77777777777777777777777d1111dddd11d11dd5555555dd11d1ddddd1111dd9999999976677777777777777777777777777777766669999999999999999999999999999999999999999999766777777
    777777777777777777777766d1111ddddddd111dd555511111ddddd11111dd99999999996667777777777777777777777777776666699999999999999999999999999999999999999999999966677777
    777777777777777777776666dd11111ddddd11111d5d11111dddd111111dddddddddddddd66667777777777777777777777766666699999999999999999999999999999999999dddddddddddd6666777
    6777777777777777766666667ddd11111dddd11111d11111ddd11111dddddddddddddddddd6666666777777777777777766666667999999999999999999999999999999999dddddddddddddddd666666
    666666666666666666666679777dddd1111ddd11ddddd11dd1111ddddddddddddddddddddddd666666666666666666666666667999999999999999999999999999999999dddddddddddddddddddd6666
    6666666666666666666679997111111ddddddddd11111ddddddddd111111dddddddddddddddddd66666666666666666666667999999999999999999999999999999999dddddddddddddddddddddddd66
    d6666666666666666799999971111111111dddd1111111dddd11111111177dddddddddddddddddddd6666666666666666799999999999999999999999999999999999ddddddddddddddddddddddddddd
    ddddd7777999999999999999977111111dddddddd111dddddddd11111777ddddddddddddddddddddddddd77779999999999999999999999999999999999999999999dddddddddddddddddddddddddddd
    dddddd77799999999999999999977777dd7d11ddddddddd111dddddd77dddddddddddddddddddddddddddd777999999999999999999999999999999999999999999ddddddddddddddddddddddddddddd
    ddddddd79999999999999999999ddddd771111d111dddd11111177dddd77ddddddd77777ddddddddddddddd79999999999999999999999999999999999999999999dddddddddddddddd77777dddddddd
    ddddddd799999999999999999bddddd7711111d1111ddd711111177dddd77dddddddd7777777ddddddddddd799999999999999999b6666666667999999999999997dddddddddddddddddd7777777dddd
    dddddd7999999999999999999ddddd7711111dd11111dd77111111777777dddddddddd7777777777dddddd7999999999999999999bb666666666667999999999997ddddddddddddddddddd7777777777
    7777d799999999999999999997bddd711111d6dd1111dd997d11111ddddddddddddddddd777777777777d799999999999999999997b6666666666666799999999997dddddddddddddddddddd77777777
    7777799999999999966b7999997b66d111dd666d11111d9999dddddddddddddddddddddddd7799977777799999999999966b7999997b6666666666666699999999977ddddddddddddddddddddd779997
    999999999999999966666679999bb66ddd666666d1111d99999977dddddddddddddddddddddd7999999999999999999966666679999bb6666666666666699999999977dddddddddddddddddddddd7999
    99999999999999966666666b9997b666666666666d111d9999999777ddddddddddddddddd777799999999999999999966666666b9997b666666666666667999999999777ddddddddddddddddd7777999
    9999999999999966666666666b99bb666666666666ddd999999999777777777777777777777799999999999999999966666666666b99bb66666666666666999999999977777777777777777777779999
    99999999999996666666666666677b6666666666666697777669999977777777777777777999999999999999999996666666666666677b66666666666666977776699999777777777777777779999999
    9999999999999666666666666666666666666666667777777769999999999999999999999999999999999999999996666666666666666666666666666677777777699999999999999999999999999999
    `)
game.showLongText("once apon a time, there was a kingdom, the kingdom of RANDOM RPG GAME LAND and in that kingdom, you are ERKY, a human who lives in the town of yellowflower.", DialogLayout.Bottom)
house1_hitbox = sprites.create(assets.image`doorvertical`, SpriteKind.outofhouse1door)
tiles.setCurrentTilemap(tilemap`world`)
tiles.placeOnTile(house1_hitbox, tiles.getTileLocation(8, 9))
mySprite = sprites.create(img`
    . . . . . . f f f f . . . . . . 
    . . . . f f f 2 2 f f f . . . . 
    . . . f f f 2 2 2 2 f f f . . . 
    . . f f f e e e e e e f f f . . 
    . . f f e 2 2 2 2 2 2 e e f . . 
    . . f e 2 f f f f f f 2 e f . . 
    . . f f f f e e e e f f f f . . 
    . f f e f b f 4 4 f b f e f f . 
    . f e e 4 1 f d d f 1 4 e e f . 
    . . f e e d d d d d d e e f . . 
    . . . f e e 4 4 4 4 e e f . . . 
    . . e 4 f 2 2 2 2 2 2 f 4 e . . 
    . . 4 d f 2 2 2 2 2 2 f d 4 . . 
    . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
    . . . . . f f f f f f . . . . . 
    . . . . . f f . . f f . . . . . 
    `, SpriteKind.Player)
press_Z = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.quicktext)
piggy = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.piggy)
tiles.placeOnTile(mySprite, tiles.getTileLocation(8, 8))
tiles.placeOnTile(press_Z, tiles.getTileLocation(8, 7))
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
pause(100)
forever(function () {
    press_Z.setPosition(mySprite.x, mySprite.y - 25)
    info.setScore(money)
})
forever(function () {
    if (!(piggy.overlapsWith(mySprite))) {
        press_Z.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `)
    }
    if (piggy.overlapsWith(mySprite) && piggys_money_stolen == 0) {
        press_Z.setImage(assets.image`Z`)
        if (controller.A.isPressed() && piggys_money_stolen == 0) {
            piggys_money_stolen = 1
            money += 10
            press_Z.setImage(assets.image`LETTER z`)
            press_Z.startEffect(effects.spray)
            pause(100)
            effects.clearParticles(press_Z)
        }
    }
})
// movement animations an camera follow sprite
forever(function () {
    scene.cameraFollowSprite(mySprite)
    while (controller.left.isPressed()) {
        mySprite.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . f f f f f f . . . . . . 
            . . . f 2 f e e e e f f . . . . 
            . . f 2 2 2 f e e e e f f . . . 
            . . f e e e e f f e e e f . . . 
            . f e 2 2 2 2 e e f f f f . . . 
            . f 2 e f f f f 2 2 2 e f . . . 
            . f f f e e e f f f f f f f . . 
            . f e e 4 4 f b e 4 4 e f f . . 
            . . f e d d f 1 4 d 4 e e f . . 
            . . . f d d d e e e e e f . . . 
            . . . f e 4 e d d 4 f . . . . . 
            . . . f 2 2 e d d e f . . . . . 
            . . f f 5 5 f e e f f f . . . . 
            . . f f f f f f f f f f . . . . 
            . . . f f f . . . f f . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . f f f f f f . . . . . . 
            . . . f 2 f e e e e f f . . . . 
            . . f 2 2 2 f e e e e f f . . . 
            . . f e e e e f f e e e f . . . 
            . f e 2 2 2 2 e e f f f f . . . 
            . f 2 e f f f f 2 2 2 e f . . . 
            . f f f e e e f f f f f f f . . 
            . f e e 4 4 f b e 4 4 e f f . . 
            . . f e d d f 1 4 d 4 e e f . . 
            . . . f d d d d 4 e e e f . . . 
            . . . f e 4 4 4 e e f f . . . . 
            . . . f 2 2 2 e d d 4 . . . . . 
            . . . f 2 2 2 e d d e . . . . . 
            . . . f 5 5 4 f e e f . . . . . 
            . . . . f f f f f f . . . . . . 
            . . . . . . f f f . . . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . f f f f f f . . . . . . 
            . . . f 2 f e e e e f f . . . . 
            . . f 2 2 2 f e e e e f f . . . 
            . . f e e e e f f e e e f . . . 
            . f e 2 2 2 2 e e f f f f . . . 
            . f 2 e f f f f 2 2 2 e f . . . 
            . f f f e e e f f f f f f f . . 
            . f e e 4 4 f b e 4 4 e f f . . 
            . . f e d d f 1 4 d 4 e e f . . 
            . . . f d d d e e e e e f . . . 
            . . . f e 4 e d d 4 f . . . . . 
            . . . f 2 2 e d d e f . . . . . 
            . . f f 5 5 f e e f f f . . . . 
            . . f f f f f f f f f f . . . . 
            . . . f f f . . . f f . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . . 
            `)
    }
    while (controller.up.isPressed()) {
        mySprite.setImage(img`
            . . . . . . f f f f . . . . . . 
            . . . . f f e e e e f f . . . . 
            . . . f e e e f f e e e f . . . 
            . . f f f f f 2 2 f f f f f . . 
            . . f f e 2 e 2 2 e 2 e f f . . 
            . . f e 2 f 2 f f 2 f 2 e f . . 
            . . f f f 2 2 e e 2 2 f f f . . 
            . f f e f 2 f e e f 2 f e f f . 
            . f e e f f e e e e f e e e f . 
            . . f e e e e e e e e e e f . . 
            . . . f e e e e e e e e f . . . 
            . . e 4 f f f f f f f f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . f f f f . . . . . . 
            . . . . f f e e e e f f . . . . 
            . . . f e e e f f e e e f . . . 
            . . . f f f f 2 2 f f f f . . . 
            . . f f e 2 e 2 2 e 2 e f f . . 
            . . f e 2 f 2 f f f 2 f e f . . 
            . . f f f 2 f e e 2 2 f f f . . 
            . . f e 2 f f e e 2 f e e f . . 
            . f f e f f e e e f e e e f f . 
            . f f e e e e e e e e e e f f . 
            . . . f e e e e e e e e f . . . 
            . . . e f f f f f f f f 4 e . . 
            . . . 4 f 2 2 2 2 2 e d d 4 . . 
            . . . e f f f f f f e e 4 . . . 
            . . . . f f f . . . . . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . f f f f . . . . . . 
            . . . . f f e e e e f f . . . . 
            . . . f e e e f f e e e f . . . 
            . . f f f f f 2 2 f f f f f . . 
            . . f f e 2 e 2 2 e 2 e f f . . 
            . . f e 2 f 2 f f 2 f 2 e f . . 
            . . f f f 2 2 e e 2 2 f f f . . 
            . f f e f 2 f e e f 2 f e f f . 
            . f e e f f e e e e f e e e f . 
            . . f e e e e e e e e e e f . . 
            . . . f e e e e e e e e f . . . 
            . . e 4 f f f f f f f f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . f f f f . . . . . . 
            . . . . f f e e e e f f . . . . 
            . . . f e e e f f e e e f . . . 
            . . . f f f f 2 2 f f f f . . . 
            . . f f e 2 e 2 2 e 2 e f f . . 
            . . f e f 2 f f f 2 f 2 e f . . 
            . . f f f 2 2 e e f 2 f f f . . 
            . . f e e f 2 e e f f 2 e f . . 
            . f f e e e f e e e f f e f f . 
            . f f e e e e e e e e e e f f . 
            . . . f e e e e e e e e f . . . 
            . . e 4 f f f f f f f f e . . . 
            . . 4 d d e 2 2 2 2 2 f 4 . . . 
            . . . 4 e e f f f f f f e . . . 
            . . . . . . . . . f f f . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . f f f f . . . . . . 
            . . . . f f e e e e f f . . . . 
            . . . f e e e f f e e e f . . . 
            . . f f f f f 2 2 f f f f f . . 
            . . f f e 2 e 2 2 e 2 e f f . . 
            . . f e 2 f 2 f f 2 f 2 e f . . 
            . . f f f 2 2 e e 2 2 f f f . . 
            . f f e f 2 f e e f 2 f e f f . 
            . f e e f f e e e e f e e e f . 
            . . f e e e e e e e e e e f . . 
            . . . f e e e e e e e e f . . . 
            . . e 4 f f f f f f f f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . . 
            `)
    }
    while (controller.down.isPressed()) {
        mySprite.setImage(img`
            . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . f f e 2 f f f f f f 2 e f f . 
            . f f f f f e e e e f f f f f . 
            . . f e f b f 4 4 f b f e f . . 
            . . f e 4 1 f d d f 1 4 e f . . 
            . . . f e 4 d d d d 4 e f e . . 
            . . f e f 2 2 2 2 e d d 4 e . . 
            . . e 4 f 2 2 2 2 e d d e . . . 
            . . . . f 4 4 5 5 f e e . . . . 
            . . . . f f f f f f f . . . . . 
            . . . . f f f . . . . . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f e e 2 2 2 2 2 2 e f f . . 
            . f f e 2 f f f f f f 2 e f f . 
            . f f f f f e e e e f f f f f . 
            . . f e f b f 4 4 f b f e f . . 
            . . f e 4 1 f d d f 1 4 e f . . 
            . . e f e 4 d d d d 4 e f . . . 
            . . e 4 d d e 2 2 2 2 f e f . . 
            . . . e d d e 2 2 2 2 f 4 e . . 
            . . . . e e f 5 5 4 4 f . . . . 
            . . . . . f f f f f f f . . . . 
            . . . . . . . . . f f f . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . . 
            `)
    }
    while (controller.right.isPressed()) {
        mySprite.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . f f f f f f . . . . 
            . . . . f f e e e e f 2 f . . . 
            . . . f f e e e e f 2 2 2 f . . 
            . . . f e e e f f e e e e f . . 
            . . . f f f f e e 2 2 2 2 e f . 
            . . . f e 2 2 2 f f f f e 2 f . 
            . . f f f f f f f e e e f f f . 
            . . f f e 4 4 e b f 4 4 e e f . 
            . . f e e 4 d 4 1 f d d e f . . 
            . . . f e e e 4 d d d d f . . . 
            . . . . 4 d d e 4 4 4 e f . . . 
            . . . . e d d e 2 2 2 2 f . . . 
            . . . . f e e f 4 4 5 5 f f . . 
            . . . . f f f f f f f f f f . . 
            . . . . . f f . . . f f f . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . f f f f f f . . . . 
            . . . . f f e e e e f 2 f . . . 
            . . . f f e e e e f 2 2 2 f . . 
            . . . f e e e f f e e e e f . . 
            . . . f f f f e e 2 2 2 2 e f . 
            . . . f e 2 2 2 f f f f e 2 f . 
            . . f f f f f f f e e e f f f . 
            . . f f e 4 4 e b f 4 4 e e f . 
            . . f e e 4 d 4 1 f d d e f . . 
            . . . f e e e 4 d d d d f . . . 
            . . . . f f e e 4 4 4 e f . . . 
            . . . . . 4 d d e 2 2 2 f . . . 
            . . . . . e d d e 2 2 2 f . . . 
            . . . . . f e e f 4 5 5 f . . . 
            . . . . . . f f f f f f . . . . 
            . . . . . . . f f f . . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . f f f f f f . . . . 
            . . . . f f e e e e f 2 f . . . 
            . . . f f e e e e f 2 2 2 f . . 
            . . . f e e e f f e e e e f . . 
            . . . f f f f e e 2 2 2 2 e f . 
            . . . f e 2 2 2 f f f f e 2 f . 
            . . f f f f f f f e e e f f f . 
            . . f f e 4 4 e b f 4 4 e e f . 
            . . f e e 4 d 4 1 f d d e f . . 
            . . . f e e e e e d d d f . . . 
            . . . . . f 4 d d e 4 e f . . . 
            . . . . . f e d d e 2 2 f . . . 
            . . . . f f f e e f 5 5 f f . . 
            . . . . f f f f f f f f f f . . 
            . . . . . f f . . . f f f . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . f f f f f f . . . . 
            . . . . f f e e e e f 2 f . . . 
            . . . f f e e e e f 2 2 2 f . . 
            . . . f e e e f f e e e e f . . 
            . . . f f f f e e 2 2 2 2 e f . 
            . . . f e 2 2 2 f f f f e 2 f . 
            . . f f f f f f f e e e f f f . 
            . . f f e 4 4 e b f 4 4 e e f . 
            . . f e e 4 d 4 1 f d d e f . . 
            . . . f e e e 4 d d d d f . . . 
            . . . . f f e e 4 4 4 e f . . . 
            . . . . . 4 d d e 2 2 2 f . . . 
            . . . . . e d d e 2 2 2 f . . . 
            . . . . . f e e f 4 5 5 f . . . 
            . . . . . . f f f f f f . . . . 
            . . . . . . . f f f . . . . . . 
            `)
        pause(200)
        mySprite.setImage(img`
            . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . . 
            `)
    }
})
