package factory.service;

import org.junit.jupiter.api.Test;
import factory.model.Circle;
import factory.model.Square;
import factory.model.Triangle;

import static org.junit.jupiter.api.Assertions.*;

class ShapeFactoryTest {
    @Test
    void drawCircle() {
        ShapeFactory shapeFactory = new ShapeFactory();
        assertTrue(shapeFactory.getShape("circle") instanceof Circle);
    }

    @Test
    void drawSquare() {
        ShapeFactory shapeFactory = new ShapeFactory();
        assertTrue(shapeFactory.getShape("square") instanceof Square);
    }

    @Test
    void drawTriangle() {
        ShapeFactory shapeFactory = new ShapeFactory();
        assertTrue(shapeFactory.getShape("triangle") instanceof Triangle);
    }

    @Test
    void drawNull() {
        ShapeFactory shapeFactory = new ShapeFactory();
        assertNull(shapeFactory.getShape(""));
    }

    @Test
    void drawNonExisting() {
        ShapeFactory shapeFactory = new ShapeFactory();
        assertNull(shapeFactory.getShape("pentagram"));
    }
}
