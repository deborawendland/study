package factory.pattern.service;

import factory.pattern.model.Circle;
import factory.pattern.model.Shape;
import factory.pattern.model.Square;
import factory.pattern.model.Triangle;

public class ShapeFactory {

    public Shape getShape(String shapeType) {
        if (shapeType == null) {
            return null;
        } else if (shapeType.equalsIgnoreCase("circle")) {
            return new Circle();
        } else if (shapeType.equalsIgnoreCase("square")) {
            return new Square();
        } else if (shapeType.equalsIgnoreCase("triangle")) {
            return new Triangle();
        } else {
            return null;
        }
    }

}
